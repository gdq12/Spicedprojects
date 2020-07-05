import slack
from sqlalchemy import create_engine
from config import OauthToken
import logging
from datetime import datetime
import time

# conenct to postgres
engine=create_engine('postgres://postgres:xxxx@my_postgresdb:5432/postgres')

# connect to slack bot
oauth_token=OauthToken
client=slack.WebClient(token=oauth_token)

def neededQueries(time1, time2):
    totalCount=f"""select count(*) from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as num_tweets;"""
    totalCount1=str(engine.execute(totalCount).first()).strip(')').strip('(').strip(',')
    rtCount=f"""select count(tweet_text) from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as hourly_report where tweet_text @@ to_tsquery('RT@');"""
    rtCount1=str(engine.execute(rtCount).first()).strip(')').strip('(').strip(',')
    berlinCount=f"""select count(location) from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as hourly_report where location @@ to_tsquery('Berlin');"""
    berlinCount1=str(engine.execute(berlinCount).first()).strip(')').strip('(').strip(',')
    deCount=f"""select count(location) from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as hourly_report where location @@ to_tsquery('Germany | Deutschland');"""
    deCount1=str(engine.execute(deCount).first()).strip(')').strip('(').strip(',')
    multiTweeters=f"""select (select count(*) from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as num_tweets)-(select count(distinct user_name) from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as hourly_report);"""
    multiTweeters1=str(engine.execute(multiTweeters).first()).strip(')').strip('(').strip(',')
    hashtagCount=f"""select count(*) from (select hashtags, tweet_text from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as hourly_report where to_tsvector(hashtags || ' ' || tweet_text) @@ plainto_tsquery('#Berlin')) as hourly_count;"""
    hashtagCount1=str(engine.execute(hashtagCount).first()).strip(')').strip('(').strip(',')
    happyTweet=f"""select tweet_text from (select sentiment_score, tweet_text from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as hourly_report order by sentiment_score desc) as max_sent limit 1;"""
    happyTweet1=str(engine.execute(happyTweet).first()).strip(')').strip('(').strip(',')
    sadTweet=f"""select tweet_text from (select sentiment_score, tweet_text from (select * from tweetpostgres where tweepy_time between '{time1}' and '{time2}') as hourly_report order by sentiment_score asc) as min_sent limit 1;"""
    sadTweet1=str(engine.execute(sadTweet).first()).strip(')').strip('(').strip(',')
    return totalCount1, rtCount1, berlinCount1, deCount1, multiTweeters1, hashtagCount1, happyTweet1, sadTweet1

while True:
    time1=datetime.utcnow()
    time1Str=time1.strftime('%B %d, %y %H:%M:%S')
    time.sleep(60*59)
    time2=datetime.utcnow()
    time2Str=time2.strftime('%B %d, %y %H:%M:%S')
    totalCount, rtCount, berlinCount, deCount, multiTweeters, hashtagCount, happyTweet, sadTweet=neededQueries(time1, time2)
    logging.critical(client.chat_postMessage(channel='#random', text=f'Hey allspicers! Your annoying tweet informant here :D, got for the following berlin tweets from {time1Str} to {time2Str}'))
    logging.critical(client.chat_postMessage(channel='#random', text=f'There were a total of {totalCount} tweets that mentioned Berlin. {rtCount} were retweets, {berlinCount} geo-tagged as Berlin, {deCount} were geo-tagged as Germany, {hashtagCount} times #Berlin was used, {multiTweeters} tweeted more than once within the timespan.'))
    logging.critical(client.chat_postMessage(channel='#random', text=f'The tweet that might of bummed out your vibe recently: {sadTweet}'))
    logging.critical(client.chat_postMessage(channel='#random', text=f'And last but not least the tweet that may have rocked your world recently: {happyTweet}'))
    logging.critical(client.chat_postMessage(channel='#random', text=f'Thats all for now, but no worries be back soon with some more annoying tweet messages :P'))

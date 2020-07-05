import logging
import time
from pymongo import MongoClient
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

#connecting to my_mongodb:twitter:tweets
client=MongoClient(host='my_mongodb', port=27017) #connex enter container, then enter port
db=client.twitter #connecting to db in mongodb container
mongoTweets=db.tweets #connecting to tweets collection in twitter db of the mongodb container

#connecting to the postgres container
#string in the following format: postgres:dbUser:dbPassword:@dbHost:dbPort/dbDBname
engine=create_engine('postgres://postgres:xxxx@my_postgresdb:5432/postgres')

#define query for postgres table creation
create_query="""CREATE TABLE IF NOT EXISTS tweetPostgres(user_time TEXT, tweepy_time TIMESTAMP, user_real TEXT, user_name TEXT, location TEXT, hashtags TEXT, tweet_text TEXT, sentiment_score REAL);"""

#initiate postgres table formation
engine.execute(create_query)
logging.critical('@ETL container, connecting to postgresdb and creating table!!!!')

#instatiate sentiment analyzer
s=SentimentIntensityAnalyzer()

# extract the tweet info from mongoDB
def extraction(time1, time2):
    mongo_dict=list(mongoTweets.find({"tweepy time":{'$gte':time1, '$lte':time2}}))
    logging.critical('@ETL container, connecting to mongodb!!!!!')
    return mongo_dict

# calculates the sentimental value to every tweet
def transformation(mongo_dict, s):
    analyzed_tweets=[]
    for tweet in mongo_dict: #takes whole dictionary tweet from mongodb
        sentiment=s.polarity_scores(tweet['text']) #calculates the sentiment score for the text value (which is string in this case)
        tweet['sentiment_score']=sentiment['compound'] #creates a new key in tweet dictionary and saves the compound sentiment score as its value
        analyzed_tweets.append(tweet) #updates the tweet dictionary with the sentiment key:value
        logging.critical('@ETL container, calculating tweet sentiment factor!!!!!!')
    return analyzed_tweets

#transfer tweet dictionary to postgresdb
def load2postgres(analyzed_tweets):
    for tweet in analyzed_tweets:
        insert_query=f"""INSERT INTO tweetPostgres VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"""
        tweetData=[tweet['User time'], tweet['tweepy time'], tweet['user'], tweet['username'], tweet['location'], tweet['hashtags'], tweet['text'], tweet['sentiment_score']]
        engine.execute(insert_query, tweetData)
        logging.critical('@ETL container, adding tweet info to postgredb table!!!!!')

while True:
    time1=datetime.utcnow()
    time.sleep(90)
    time2=datetime.utcnow()
    mongo_dict=extraction(time1, time2)
    analyzed_tweets=transformation(mongo_dict, s)
    load2postgres(analyzed_tweets)

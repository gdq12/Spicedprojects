import config
import time
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json
import logging
from pymongo import MongoClient
from datetime import datetime

#create connection to mongodb
client=MongoClient(host='my_mongodb', port=27017) #connex to mongodb container in docker-compose
db=client.twitter #creating the db in mongodb
tweets=db.tweets #creating the collection that will store all in the dictionaries within db in mongo


def authenticate():
    """
    To create authentication token for twitter, the necessary credentials should be in the config.py file
    """
    auth = OAuthHandler(config.CONSUMER_API_KEY, config.CONSUMER_API_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    return auth

class TwitterListener(StreamListener):
#this is a function that retrieves data from every tweet by scanning specific tweets based on filter
    def on_data(self, data):
    #retrieves data from StreamListener on_status method
        t = json.loads(data) #all meta data from tweet saved into a json dictionary
        logging.warning('---------------Incoming Tweet!!!!!!---------------') #print message in terminal tweet detected

        #extract all desired info from dictionary for mongo
        hashtags=[]

        if t['created_at'] != None:
            try:
                timeStamp=t['created_at']
            except KeyError:
                timeStamp='Not provided'

        if t['user']['name'] != None:
            try:
                user=t['user']['name']
            except KeyError:
                user='Not provided'

        if t['user']['screen_name'] != None:
            try:
                username=t['user']['screen_name']
            except KeyError:
                username='Not provided'

        try:
            location=t['user']['location']
        except KeyError:
            location='Not provided'

        if 'extended_tweet' in t:
            for hashtag in t['extended_tweet']['entities']['hashtags']:
                hashtags.append(hashtag['text'])
        elif 'hashtags' in t['entities'] and len(t['entities']['hashtags']) > 0:
            hashtags=[item['text'] for item in t['entities']['hashtags']]

        if 'extended_tweet' in t:
            text=t['extended_tweet']['full_text']
        else:
            text=t['text']

        #save specific info into custom dictionary for mongodb
        tweet = {'User time':timeStamp, 'tweepy time':datetime.utcnow(), 'user':user, 'username':username, 'location':location, 'hashtags':hashtags,'text':text}

        tweets.insert_many([tweet]) #to add tweet dictionary into mongodb collection
        logging.critical('Successfully added to mongoDB!!!!!!!') #indicate in terminal data transfered to mongodb container
        logging.warning('-------------------------------------') #asthetic printing for terminal

    def on_error(self, status):
        if status == 420:
            print(status)
            return False

    def on_limit(self, status):
        print('Rate Limit Exceeded, sleep for 6 minutes')
        time.sleep(6*60)
        return True

if __name__ == '__main__':

    auth = authenticate()
    listener = TwitterListener()
    stream = Stream(auth, listener)
    stream.filter(track=['berlin'], languages=['en'])
    # can customize filter to any other word

from pymongo import MongoClient
import pprint
import json
import os.path
import path


client = MongoClient()
db = client.test
collection = db.sample_tweets

def only_relevant(tweet):
    relevant = {}

    
    relevant['created_at'] = tweet['created_at']
    relevant['hashtags'] = tweet['entities']['hashtags']
    #relevant['media'] = tweet['entities']['media']
    #relevant['media_url'] = tweet['entities']['media']['media_url']
    relevant['urls'] = tweet['entities']['urls']
    relevant['user_mentions_name'] = tweet['entities']['user_mentions']['name']
    relevant['user_mentions_screen_name'] = tweet['entities']['user_mentions']['screen_name']
    relevant['favorite_count'] = tweet['favorite_count']
    relevant['in_reply_to'] = tweet['in_reply_to_screen_name']
    #relevant['location_country'] = tweet['place']['country']
    #relevant['location_name'] = tweet['place']['full_name']
    relevant['retweet_count'] = tweet['retweeted_status']['retweet_count']
    relevant['retweeted_name'] = tweet['retweeted_status']['user']['name']
    relevant['retweeted_screen_name'] = tweet['retweeted_status']['user']['screen_name']
    #relevant['source'] = tweet['source']
    #relevant['text'] = tweet['text']
    #relevant['user_description'] = tweet['user']['description']
    relevant['user_screen_name'] = tweet['user']['screen_name']
    relevant['user_followers'] = tweet['user']['followers_count']
    relevant['user_friends'] = tweet['user']['friends_count']
    relevant['user_tweet_total'] = tweet['user']['statuses_count']
    relevant['user_location'] = tweet['user']['location']
    relevant['user_name'] = tweet['user']['name']
    relevant['user_url'] = tweet['user']['url']

    
    return relevant


S_DIR = "/Users/Kellie/Desktop/"


with open(os.path.join(S_DIR, 'geotagged_tweets_20160812-0912.json'), 'rb') as rf:
    
    for line in rf:
        tweet = (json.loads(line))
        if 'Aug' in tweet['created_at']:
        #filtered = only_relevant(tweet)
        #print(tweet['created_at'])
            collection.insert_one(tweet)
        elif 'Jul' in tweet['created_at']:
            collection.insert_one(tweet)
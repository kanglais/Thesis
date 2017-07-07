
from pymongo import MongoClient
import os
import json

client = MongoClient()
db = client.tweets
collection = db.tweets_with_urls

#^^created new collection w/in database

S_DIR = '/var/storage438/datastore/srudinac/twitter_data/'

counter = 0

user_topics = {}


with open(os.path.join(S_DIR, 'election_tweets_20160812.json'), 'rb') as rf:

    for line in rf:

        tweet = json.loads(line)

        if tweet['user']['id_str'] not in user_topics:

            user_topics[tweet['user']['id_str']] = []

        for created in tweet['created_at']:

            user_topics[tweet['user']['id_str']].append(['created_at'])

        for hashtag in tweet['entities']['hashtags']:

            user_topics[tweet['user']['id_str']].append(hashtag['text'])

        for user in tweet['entities']['user_mentions']:

            user_topics[tweet['user']['id_str']].append(user['screen_name'])

        for url in tweet['entities']['urls']:

            user_topics[tweet['user']['id_str']].append(url['expanded_url'])

        counter+=1

        collection.insert_many(user_topics, ordered=False)
        
        if counter%10000==0: 
            print('so far, ' + str(counter))



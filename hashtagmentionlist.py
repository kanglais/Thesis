from pymongo import MongoClient
import json
import numpy as np
from sklearn import preprocessing


client = MongoClient()
db = client.test
collection = db.tweets

vocabulary = list(set(handles))

users_hash_mentions = []

hash_list = []
mention_list = []
full_list = []
unique_hash = set()
unique_mention = set()

for doc in collection.find({'user.screen_name': {'$exists': 'true'}}):
    hashtags = doc['entities']['hashtags']
    mentions = doc['entities']['user_mentions']

    for tag in hashtags:
        unique_hash.add(tag['text'])
        hash_list.append(tag['text'])

    for mention in mentions:
        unique_mention.add(mention['screen_name'])
        mention_list.append(mention['screen_name'])

unique = unique_hash | unique_mention

for doc in collection.find({'user.screen_name': {'$exists' : 'true'}}):
    
    each_user = []
    
    hashtags = doc['entities']['hashtags']
    mentions = doc['entities']['user_mentions']

    for item in vocabulary: 
        if item in hashtags:
            each_user.append(1)

        elif item in mentions:
            each_user.append(1)
            
        else: 
            each_user.append(0)
                
    users_hash_mentions.append(each_user)
    #print(each_user)
        
matrix = np.array(users_hash_mentions)

preprocessing.normalize(matrix)
#using mongodb tutorial 

import json
from pymongo import MongoClient

client = MongoClient() 
db = client.sample_tweet

coll = db.dataset

#Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), u'sample_tweet')

S_DIR = "/Users/Kellie/Desktop/thesis/geotagged_tweets_20160812-0912.json"

tweets = []

with open(S_DIR, 'r') as f:
	line = f.readline()
	tweet = json.loads(line)
	tweets.append(json.loads(line))
	print(json.dumps(tweet, indent=4))


hashtags = ['#donaldtrump', '#trumppence16', '#crookedhillary', '#hillaryclinton', '#trump', '#nevertrump', '#imwithher',
'#dumptrump','#hillaryclinton', '#imwithher', '#crookedhillary', '#maga', '#trump', '#trumppence16', '#nevertrump', '#hillary', '#neverhillary','@realDonaldTrump', '@HillaryClinton']

hashtags = list(set(hashtags))


from pymongo import MongoClient
import json
import os.path

client = MongoClient()
db = client.test
collection = db.tweets

doc1 = collection.find_one()

print(doc1)

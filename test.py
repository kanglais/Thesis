import json
import os

S_DIR = "/var/storage438/datastore/srudinac/twitter_data/"
D_DIR = "/var/scratch/kenglish/"

raw_tweets = {}

with open(os.path.join(S_DIR, 'election_tweets_20160812.json'), 'r') as raw_data:

	for line in raw_data:

		tweet = json.loads(line)

		if 'Jan' in tweet['user']['created_at']:

			raw_tweets[tweet['user']['id_str']] = [tweet]

output_file = open(os.path.join(S_DIR, 'jan_tweets.json'), 'w')
json.dump(raw_tweets, output_file)
output_file.close()


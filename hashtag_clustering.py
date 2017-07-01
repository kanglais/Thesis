import pprint
import json

# load tweet data as an object
with open('./data/hash_mention.json', 'rb') as raw_tweet_data:

    users_and_hash_mentions = json.load(raw_tweet_data)

    pprint.pprint(users_and_hash_mentions, width=1)




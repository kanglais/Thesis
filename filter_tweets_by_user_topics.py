
import os
import json

S_DIR = '/var/storage438/datastore/srudinac/twitter_data/'

counter = 0

user_topics = {}


with open(os.path.join(S_DIR, 'election_tweets_20160812.json'), 'rb') as rf:

    for line in rf:

        tweet = json.loads(line)

        try:

            if tweet['user']['id_str'] not in user_topics:

                user_topics[tweet['user']['id_str']] = []

            for created in tweet['created_at']:
                if 'Jan' in created:
                    user_topics[tweet['user']['id_str']].append(tweet)
                elif 'Feb' in created:
                    user_topics[tweet['user']['id_str']].append(tweet)
                elif 'Mar' in created:
                    user_topics[tweet['user']['id_str']].append(tweet)
                elif 'Apr' in created:
                    user_topics[tweet['user']['id_str']].append(tweet)
        except:
            print(tweet)

        counter+=1
        
        if counter%100000==0: 
            print('so far, ' + str(counter))


output_dir = '/var/scratch/kenglish/'

output_file = open(os.path.join(output_dir, 'hash_mention.json'), 'w')
json.dump(user_topics, output_file)
output_file.close()
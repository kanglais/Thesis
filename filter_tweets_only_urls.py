
import os
import json

S_DIR = '/Users/Kellie/Desktop/'
D_DIR = '/Users/Kellie/Desktop/'


counter = 0

user_topics = {}


with open(os.path.join(S_DIR, 'geotagged_tweets_20160812-0912.json'), 'rb') as rf:

    for line in rf:

        tweet = json.loads(line)

        try:

            if tweet['user']['id_str'] not in user_topics:

                user_topics[tweet['user']['id_str']] = []

            for url in tweet['entities']['urls']:

                user_topics[tweet['user']['id_str']].append(url['expanded_url'])

        except:
            print(tweet)

        counter+=1
        
        if counter%10000==0: 
            print('so far, ' + str(counter))



output_file = open(os.path.join(D_DIR, 'only_urls.json'), 'w')
json.dump(user_topics, output_file)
output_file.close()
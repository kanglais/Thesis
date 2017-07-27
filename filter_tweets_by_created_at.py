import json
import os.path

S_DIR = "/var/storage438/datastore/srudinac/twitter_data/" 

output_dir = '/var/scratch/kenglish/'

feb_tweets = {}
mar_tweets = {}
apr_tweets = {}

with open(os.path.join(S_DIR, 'election_tweets_20160812.json'), 'rb') as rf:

	counter = 0

    for line in rf:
        tweet = json.loads(line)

        try:

         	if 'Feb' in tweet['created_at']:

    	        feb_tweets.update([tweet])
    	        counter+=1

            elif 'Mar' in tweet['created_at']:
                mar_tweets.update([tweet])
                counter+=1
            elif 'Apr' in tweet['created_at']:
                apr_tweets.update([tweet])
                counter+=1

    	    else:
    	    	counter+=1

        except:

            print tweet.keys()

	if counter%10000==0: 
		print('so far, ' + str(counter))


feb_output_file = open(os.path.join(output_dir, 'feb_tweets.json'), 'w')
json.dump(feb_tweets, feb_output_file)
feb_output_file.close()

mar_output_file = open(os.path.join(output_dir, 'mar_tweets.json'), 'w')
json.dump(mar_tweets, mar_output_file)
mar_output_file.close()

apr_output_file = open(os.path.join(output_dir, 'apr_tweets.json'), 'w')
json.dump(apr_tweets, apr_output_file)
apr_output_file.close()
import json
import os.path

def only_relevant(tweet):
    relevant = {}

    
    relevant['created_at'] = tweet['created_at']
    relevant['hashtags'] = tweet['entities']['hashtags']
    relevant['urls'] = tweet['entities']['urls']
    relevant['mentions_screen_name'] = tweet['entities']['user_mentions']['screen_name']
    relevant['favorite_count'] = tweet['favorite_count']
    relevant['retweet_count'] = tweet['retweeted_status']['retweet_count']
    relevant['retweeted_screen_name'] = tweet['retweeted_status']['user']['screen_name']
    relevant['user_screen_name'] = tweet['user']['screen_name']
    relevant['user_followers'] = tweet['user']['followers_count']
    relevant['user_friends'] = tweet['user']['friends_count']
    relevant['user_name'] = tweet['user']['name']
    relevant['user_id'] = tweet['user']['id']
 
    
    return relevant

S_DIR = "/var/storage438/datastore/srudinac/twitter_data/" 



with open(os.path.join(S_DIR, 'election_tweets_20160812.json'), 'rb') as rf:

	counter = 0

    for line in rf:
        tweet = json.loads(line)

         	if 'Jan' in tweet['created_at']:

    			filtered = only_relevant(tweet)
    	        output.write(filtered)
    	        counter+=1

         	elif 'Feb' in tweet['created_at']:

    			filtered = only_relevant(tweet)
                output.write(filtered)
                counter+=1

         	elif 'Mar' in tweet['created_at']:

    			filtered = only_relevant(tweet)
                output.write(filtered)
                counter+=1

         	elif 'Apr' in tweet['created_at']:

    			filtered = only_relevant(tweet)
                output.write(filtered)
                counter+=1

    	    else:
    	    	continue

        except:

            print tweet.keys()
            break
	if counter%10000==0: 
		print('so far, ' + str(counter))

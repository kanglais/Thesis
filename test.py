import json
import os
import re

output_dir = './data/'    
counter = 0

#url_list = []

with open(os.path.join(output_dir, 'hash_mention.json'), 'r') as rf:
    tweet = json.loads(rf)

    print(tweet.shape())
    # for i in tweet: 
    #     for item in tweet[i]:
    #         print(item)
                #try: 
                    #url = re.search("(?P<url>https?://[^\s]+)", item)
                    #if match is not None: 
                        #print(url)
                    #url_list.append(url)
                #except:
                    #pass
        #counter+=1
        #if counter==10:
            #break
#print(url_list)
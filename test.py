import json
import os
import re

output_dir = '/Users/Kellie/Desktop/'    
counter = 0

#url_list = []

with open(os.path.join(output_dir, 'hash_mention.json'), 'r') as rf:
    for line in rf:

        tweet = json.loads(line)
        for i in tweet: 
            for item in tweet[i]:
                print(item)
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
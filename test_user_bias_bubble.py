import numpy as np 
import json
from collections import defaultdict
from urllib.parse import urlparse
from collections import Counter
import pprint
import pandas as pd

input_data_file = './data/sep_tweets.json'

with open(input_data_file, 'rb') as raw_url_data:

    all_users_full_tweets_dict = json.load(raw_url_data)

#list of all the user id's 

user_ids = list(all_users_full_tweets_dict.keys())

#break raw tweet dictionary into series of lists containing relevant info based on user ids (so order remains the same)

created_at_list = []

reply_to_sn_list = []

hashtags_list = []

url_full_list = []

user_mentions_full_list = []

user_id_list = []

user_sn_list = []


count = 0

for user in user_ids:
    
    user_id_list.append(user)
    
    for doc in all_users_full_tweets_dict[user]:
        
        created_at_list.append(doc['created_at'])
        
        user_sn_list.append(doc['user']['screen_name'])

        reply_to_sn_list.append(doc['in_reply_to_screen_name'])

        hashtags_list.append(doc['entities']['hashtags'])

        url_full_list.append(doc['entities']['urls'])

        user_mentions_full_list.append(doc['entities']['user_mentions'])
        
        count+=1
#     if count==25:
#         break


#create a dict with reply_to screen names and user id's 
#users that tweeted at other users

count = 0

reply_to_sn_dict = {}

for user in user_id_list:
    
    if user not in reply_to_sn_dict:
        reply_to_sn_dict[user] = []
    
    for doc in all_users_full_tweets_dict[user]:
        reply_to_sn_dict[user].append(doc['in_reply_to_screen_name'])
# pprint.pprint(reply_to_sn_dict)

#create dict with user ids and full data of hashtags (includes indices, etc.)
#note- should this be expanded to include mentions?

hash_dict_with_user = {}

i = 0

for user in user_id_list:
    
    for doc in all_users_full_tweets_dict[user]:
        
        hash_dict_with_user.update({user : doc['entities']['hashtags']})


#create cleaner dict with user ids and only text of hashtags as list 

user_hash_dict = {}

for user in hash_dict_with_user:
    
    if user not in user_hash_dict:
        user_hash_dict[user] = []
    
    for item in hash_dict_with_user[user]:        
        user_hash_dict[user].append(item['text'])

# print(len(user_hash_dict))

#create two lists, one of users who use urls as sources and one of users who don't use any urls

non_url_users = []

url_users = []

#create dict with only expanded_url and user id
expanded_url_dict_with_user = {}

i = 0

for item in url_full_list:
    if item == []:
        non_url_users.append(user_id_list[i])
    else:
        url_users.append(user_id_list[i])        
        for url in item:   
            expanded_url_dict_with_user.update({user_id_list[i] : [url['expanded_url']]})
    i+=1


#news sources as defined by pew research center
news_sources = np.array(['breitbart', 'limbaugh', 'theblaze', 'hannity', 'glenbeck', 'drudgereport', 'fox',
                'wallstreetjournal', 'yahoo', 'usatoday', 'abc', 'bloomberg', 'google', 'cbs', 'nbc',
                'cnn', 'msnbc', 'buzzfeed', 'pbs', 'bbc', 'huffingtonpost', 'washingtonpost', 'economist', 'politico',
                'dailyshow', 'guardian', 'aljazeera', 'npr', 'colbertreport', 'nytimes', 'slate', 'newyorker'])


#create cooccurence matrix 
def create_cooc_matrix(data, standardize = False):
    cooc_m = np.zeros((data.shape[1], data.shape[1]))
    for i, c1 in enumerate(data.T):
        for j, c2 in enumerate(data.T):
            cooc_m[i,j] = np.sum(c1*c2)
    if standardize:
        return cooc_m / data.shape[0]
    return cooc_m

#determine user bias based on sources used

count = 0
user_bias = []

for user_id in expanded_url_dict_with_user:
    
    user_sources = []
        
    #to create array of zeros:
    user_zero_vector_bias = list(np.zeros(len(news_sources)))
    
    #get root urls of expanded urls using url parse python library
    url_item = expanded_url_dict_with_user[user_id]
    for item in url_item:
        o = urlparse(item)
        root_url = o.hostname
        root_name_only = root_url.split(".")
        
        #root urls were split, remove the irrelevant stuff 
        if root_name_only[0] == "www":
            user_sources.append(root_name_only[1])
        else:
            user_sources.append(root_name_only[0])
        user_sources.append(root_url)
    
    #create vectors with counts for every time a source is used, and 0's otherwise
    for i, source in enumerate(news_sources):            

        user_zero_vector_bias[i] = int(source in user_sources)

    user_bias.append(user_zero_vector_bias)

    count +=1

#     if count==500:
#         break

#print(count)
# print(len(user_bias))

#turn the list of vectors from above into a matrix
bias_matrix = np.array(user_bias)

#run matrix through cooccurrence function
a = create_cooc_matrix(bias_matrix)

# b = (a/np.diagonal(a)).T

#bias, according to pew research center

bias = np.array([0.6, 0.6, 0.6, 0.6, 0.6, 0.5, 0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2, -0.2, -0.3,
        -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.6, -0.6])


#create matrix of user bias using pew results: 
#1 if user used source, 0 if not

def create_bias_matrix(data, news_sources):
    bias_value_return_list = []

    user_sources = []
    
    count = 0

    for user_id in data:

        #to create array of zeros:
        user_zero_vector_bias = list(np.zeros(len(news_sources)))
        
        # what sources *did* this user use        
        url_item = expanded_url_dict_with_user[user_id]
        for item in url_item:
            o = urlparse(item)
            root_url = o.hostname
            root_url_split = root_url.split(".")
            
            if root_url_split[0] == "www":
                user_sources.append(root_url_split[1])
            else:
                user_sources.append(root_url_split[0])
                    
        # print(bias_value_return_list)
                    
        for i, source in enumerate(news_sources):            
            user_zero_vector_bias[i] = user_sources.count(source)
#             if source in root_url_split:
#                 user_zero_vector_bias[i]+=1
            
        bias_value_return_list.append(user_zero_vector_bias)

        count +=1
        
#         if count==500:
#             break
            #print(count)
    return bias_value_return_list

# print(user_bias[:1000])

#create matrix using url dict
user_sources_count = create_bias_matrix(expanded_url_dict_with_user, news_sources)

#transform into matrix
user_sources_matrix = np.array(user_sources_count)

#multiply results by bias measure from pew

user_bias_measure_pew = []

for user in user_sources_matrix:
    user_bias_measure_pew.append(user*bias)


#transform to matrix

user_bias_measure_pew = np.array(user_bias_measure_pew)

#transpose of matrix 

user_bias_measure_pew = user_bias_measure_pew.T

#sum columns (users) of matrix 

i = 0

while i < len(user_bias_measure_pew):
    
    bias_number_user = list(sum(user_bias_measure_pew))
    i+=1


#associate user ID's with user bias again

users_and_biases =[[str(u),b] for u,b in zip(url_users,bias_number_user)]


#determine bias based on positive or negative results

liberal_users = []
conservative_users = []
neutral_users = []

for user in users_and_biases:
    if user[1] > 0:
        conservative_users.append(user[0])
    elif user[1] < 0:
        liberal_users.append(user[0])
    elif user[1] == 0:
        neutral_users.append(user[0])
        
print(len(conservative_users))
print(len(liberal_users))
print(len(neutral_users))


#determine which hashtags are more common with which biases

liberal_tags = []
conservative_tags = []
neutral_tags = []
non_url_tags = []

all_hashtags = []


for user in user_hash_dict:
    
    all_hashtags.append(user_hash_dict[user])
    
    if user in liberal_users:
        liberal_tags.append(user_hash_dict[user])
    elif user in conservative_users:
        conservative_tags.append(user_hash_dict[user])
    elif user in neutral_users:
        neutral_tags.append(user_hash_dict[user])
    elif user in non_url_users:
        non_url_tags.append(user_hash_dict[user])
    else:
        print(user)

#create list of unique hashtags, liberal

liberal_unique = []

for tag in liberal_tags: 
    for item in tag: 
        liberal_unique.append(item)

liberal_unique = set(liberal_unique)

# print(liberal_unique)

#create list of unique hashtags, conservative

conservative_unique = []

for tag in conservative_tags: 
    for item in tag: 
        conservative_unique.append(item)
conservative_unique = set(conservative_unique) 


#create list of unique hashtags, neutral

neutral_unique = []

for tag in neutral_tags: 
    for item in tag: 
        neutral_unique.append(item)
neutral_unique = set(neutral_unique)



#associate screen names and user id's with bias

ids_and_sn =[[str(u),sn] for u,sn in zip(user_id_list,user_sn_list)]

#define users according to their potential bias based on tweeted sources

conservative_screen_names = []
liberal_screen_names = []
neutral_screen_names = []
non_url_user_screen_names = []

for i, u in ids_and_sn:
    if i in conservative_users:
        conservative_screen_names.append(u)
    elif i in liberal_users:
        liberal_screen_names.append(u)
    elif i in neutral_users:
        neutral_screen_names.append(u)
    else:
        non_url_user_screen_names.append(u)
print(len(non_url_user_screen_names))

#see which non-url using users retweeted which biased users
#define potential bias of non_url users

maybe_conservative_retweet_bias = []
maybe_liberal_retweet_bias = []
maybe_neutral_retweet_bias = []


for user in reply_to_sn_dict:
    
    if user in non_url_users:
        rt = reply_to_sn_dict[user]
        for text in rt: 
            if text in conservative_screen_names:
                maybe_conservative_retweet_bias.append(user)
            elif text in liberal_screen_names:
                maybe_liberal_retweet_bias.append(user)
            elif text in neutral_screen_names:
                maybe_neutral_retweet_bias.append(user)
# print(maybe_neutral)

#see what hashtags non_url users are using

liberal_hash_users = []
conservative_hash_users = []
neutral_hash_users = []
unknown_hash = []
uncertain_users = []

for user in user_hash_dict:
    if user in non_url_users:
        for text in user_hash_dict[user]: 
            if text in liberal_unique:
                liberal_hash_users.append(user)
            elif text in conservative_unique:
                conservative_hash_users.append(user)
            elif text in neutral_unique:
                neutral_hash_users.append(user)
            else:
                unknown_hash.append(text)
                uncertain_users.append(user)


#match hashtag bias with sources bias and try to confirm source bias- are they the same?

liberal_positive_results = []
conservative_positive_results = []
neutral_positive_results = []

liberal_negative_results = []
conservative_negative_results = []
neutral_negative_results = []

for user in liberal_hash_users:
    if user in maybe_liberal_retweet_bias:
        liberal_positive_results.append(user)
    else:
        liberal_negative_results.append(user)


for user in conservative_hash_users:
    if user in maybe_conservative_retweet_bias:
        conservative_positive_results.append(user)
    else:
        conservative_negative_results.append(user)

for user in neutral_hash_users:
    if user in maybe_neutral_retweet_bias:
        neutral_positive_results.append(user)
    else:
        neutral_negative_results.append(user)



print(len(liberal_positive_results))
print(len(conservative_positive_results))
print(len(neutral_positive_results))

print(len(liberal_negative_results))
print(len(conservative_negative_results))
print(len(neutral_negative_results))

print(len(uncertain_users))


#below, from test_hashtag_bias_bubble -- needs to be edited into functions!! 

from collections import Counter

one_list_hashtags = []

for tag in all_hashtags: 
    for text in tag: 
        one_list_hashtags.append(text)

frequencies_hash = Counter(one_list_hashtags)

print(frequencies_hash.most_common(100))


#manually choose liberal and conservative hashtags, fill lists

conservative_list = ['Trump', 'DonaldTrump', 'trump', 'NeverHillary', 'MAGA', 'TrumpPence16', 'CrookedHillary', 'MakeAmericaGreatAgain', 'BasketOfDeplorables', 'HillarysHealth']

liberal_list = ['ImWithHer', 'HillaryClinton', 'NeverTrump', 'Hillary', 'imwithher', 'nevertrump', 'DumpTrump', 'Clinton', 'dumptrump', 'hillary']

#split users into liberal, conservative, neutral groups based on above lists

users_conservative_hash_bias = []
users_liberal_hash_bias = []
users_neutral_hash_bias = []

for user in user_hash_dict: 
    for text in user_hash_dict[user]:
        if text in conservative_list:
            users_conservative_hash_bias.append(user)
        elif text in liberal_list:
            users_liberal_hash_bias.append(user)
        else:
            users_neutral_hash_bias.append(user)

print(len(users_conservative_hash_bias))
print(len(users_liberal_hash_bias))
print(len(users_neutral_hash_bias))


conservative_users_and_sn = []

for i, u in ids_and_sn: 
    if i in users_conservative_hash_bias:
        conservative_users_and_sn.append([i, u])


#check predominant retweets in these groups 
cons_potential = []

for i, sn in conservative_users_and_sn: 
    for user in reply_to_sn_dict:
        if sn in reply_to_sn_dict[user]:
            cons_potential.append(user)

cons_check = []

for user in cons_potential:
    if user in conservative_users_and_sn:
        cons_check.append(user)
print(len(cons_check))


liberal_users_and_sn = []

for i, u in ids_and_sn: 
    if i in users_liberal_hash_bias:
        liberal_users_and_sn.append([i, u])



#check predominant retweets in these groups 
lib_potential = []

for i, sn in liberal_users_and_sn: 
    for user in reply_to_sn_dict:
        if sn in reply_to_sn_dict[user]:
            lib_potential.append(user)

lib_check = []

for user in lib_potential:
    if user in liberal_users_and_sn:
        lib_potential.append(user)
print(len(lib_potential))

neutral_users_and_sn = []

for i, u in ids_and_sn: 
    if i in users_neutral_hash_bias:
        neutral_users_and_sn.append([i, u])

#check predominant retweets in these groups 

neu_potential = []

for i, sn in neutral_users_and_sn: 
    for user in reply_to_sn_dict:
        if sn in reply_to_sn_dict[user]:
            neu_potential.append(user)

neu_check = []

for user in neu_potential:
    if user in neutral_users_and_sn:
        neu_potential.append(user)
print(len(neu_potential))


#check predominant news sources in these groups

cons_sources = []

for i, sn in conservative_users_and_sn:
    if i in expanded_url_dict_with_user:
        for text in expanded_url_dict_with_user[i]:
            o = urlparse(text)
            root_url = o.hostname
            root_url_split = root_url.split(".")

            if root_url_split[0] == "www":
                cons_sources.append(root_url_split[1])
            else:
                cons_sources.append(root_url_split[0])

print(len(cons_sources))
print(Counter(cons_sources))

lib_sources = []

for i, sn in liberal_users_and_sn:
    if i in expanded_url_dict_with_user:
        for text in expanded_url_dict_with_user[i]:
            o = urlparse(text)
            root_url = o.hostname
            root_url_split = root_url.split(".")

            if root_url_split[0] == "www":
                lib_sources.append(root_url_split[1])
            else:
                lib_sources.append(root_url_split[0])

print(len(lib_sources))

print(Counter(lib_sources))

neu_sources = []

for i, sn in neutral_users_and_sn:
    if i in expanded_url_dict_with_user:
        for text in expanded_url_dict_with_user[i]:
            o = urlparse(text)
            root_url = o.hostname
            root_url_split = root_url.split(".")

            if root_url_split[0] == "www":
                neu_sources.append(root_url_split[1])
            else:
                neu_sources.append(root_url_split[0])

print(len(neu_sources))

print(Counter(neu_sources))

#check predominant hashtags in these groups 

top_neu_hash = []

for i, sn in neutral_users_and_sn:
    if i in user_hash_dict:
        top_neu_hash.extend(user_hash_dict[i])
print(len(top_neu_hash))

print(Counter(top_neu_hash))

top_cons_hash = []

for i, sn in conservative_users_and_sn:
    if i in user_hash_dict:
        top_cons_hash.extend(user_hash_dict[i])
print(len(top_cons_hash))

print(Counter(top_cons_hash))

top_lib_hash = []

for i, sn in liberal_users_and_sn:
    if i in user_hash_dict:
        top_lib_hash.extend(user_hash_dict[i])
print(len(top_lib_hash))

print(Counter(top_lib_hash))


import numpy as np 
import json
from collections import defaultdict
from urllib.parse import urlparse
from collections import Counter

#determine which hashtags are more common with which biases
def define_hashtag_bias(user_hash_dict, user_list_biased):
    bias_tags = []
    all_tags = []

    for user in user_hash_dict:
        all_tags.append(user_hash_dict[user])

        if user in user_list_biased:
            bias_tags.append(user_hash_dict[user])
    return bias_tags

#create list of unique hashtags
def unique_tags(tag_list):
    unique = []

    for tag in tag_list:
        for item in tag:
            unique.append(item)

    unique = set(unique)
    return unique

#define users according to their potential bias based on tweeted sources
def potential_bias(ids_and_sn, user_list):
    screen_names = []

    for i, u in ids_and_sn:
        if i in user_list:
            screen_names.append(u)
    return screen_names

#see which non-url using users retweeted which biased users
#define potential bias of non_url users
def potential_bias_based_on_retweets(reply_to_sn_dict, non_url_users, screen_name_list):
    retweet_bias = []

    for user in reply_to_sn_dict:
        if user in non_url_users:
            rt = reply_to_sn_dict[user]
            for text in rt:
                if text in screen_name_list:
                    retweet_bias.append(user)
    return(retweet_bias)
#see what hashtags non_url users are using
def non_url_user_hash(user_hash_dict, non_url_users, unique_hash_list):
    hash_users = []

    for user in user_hash_dict:
        if user in non_url_users:
            for text in user_hash_dict[user]:
                if text in unique_hash_list:
                    hash_users.append(user)
    return hash_users

def positive_and_negative_results(hash_users, retweet_bias):
	
	positive = []
	negative = []

	for user in hash_users:
	    if user in retweet_bias:
	        positive.append(user)
	    else:
	        negative.append(user)


	print('positive results are ', len(positive))
	print('negative results are', len(negative))

	return(positive, negative)


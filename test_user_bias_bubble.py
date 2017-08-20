import test_hashtag_bias_bubble
import break_tweet_into_dicts
import numpy as np 
import json
from collections import defaultdict
from urllib.parse import urlparse
from collections import Counter
import pprint
import pandas as pd

#bias, according to pew research center
bias = np.array([0.66, 0.59, 0.63, 0.55, -0.88, 0.52, 0.71, 0.69, 0.62, 0.38, 0.35, 0.72, 0.48, 0.29, 0.25, 0.38, 0.45, 
	0.36, 0.32, 0.3, -0.62, -0.58, 0.18, -0.51, 0.28, -0.34, 0.21, 0.21, -0.37, 0.25, -0.25, 0.14, 0.14, 0.06, 0.1, 0.1])


#news sources as defined by pew research center
news_sources = np.array(['cnn', 'abc', 'nbc', 'cbs', 'fox', 'msnbc', 'pbs', 'bbc', 'nytimes', 'usatoday', 
		'wallstreetjournal', 'npr', 'washingtonpost', 'google', 'yahoo', 'huffingtonpost', 'dailyshow', 'colbertreport', 
		'newyorker', 'economist', 'hannity', 'limbaugh', 'bloomberg', 'glennbeck', 'aljazeera', 'drudgereport', 'guardian', 
		'politico', 'theblaze', 'motherjones', 'breitbart', 'slate', 'edschultz', 'buzzfeed', 'dailykos', 'thinkprogress'])

def create_and_test_user_bias_matrix(input_data_file):

	all_users_full_tweets_dict = break_tweet_into_dicts.all_users_full_tweets_dict

	# with open(input_data_file, 'r') as raw_url_data:

	# 	for line in raw_url_data:
	# 		tweet = json.loads(line)

	# 		all_users_full_tweets_dict[tweet['user']['id_str']] = tweet

	#list of all the user id's 
	user_ids = break_tweet_into_dicts.user_ids

	#break raw tweet dictionary into series of lists containing relevant info 
	#based on user ids (so order remains the same)

	created_at_list = break_tweet_into_dicts.created_at_list
	reply_to_sn_list = break_tweet_into_dicts.reply_to_sn_list
	hashtags_list = break_tweet_into_dicts.hashtags_list
	url_full_list = break_tweet_into_dicts.url_full_list
	user_mentions_full_list = break_tweet_into_dicts.user_mentions_full_list
	user_id_list = break_tweet_into_dicts.user_id_list
	user_sn_list = break_tweet_into_dicts.user_sn_list

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

	reply_to_sn_dict = create_retweet_user_dict(user_id_list, all_users_full_tweets_dict)

	user_hash_dict = create_hashtag_user_dict(user_id_list, all_users_full_tweets_dict)

	#create matrix using url dict
	bias_matrix = create_bias_matrix(expanded_url_dict_with_user, news_sources)

	# cooc_diag = diagonal_cooc_matrix(cooc_matrix)
	bias_number_user = pew_bias_matrix(bias_matrix)
	users_and_biases = user_ids_user_bias(url_users, bias_number_user)


	#determine bias based on positive or negative results
	liberal_users = []
	conservative_users = []
	neutral_users = []

	for user in users_and_biases:
		if user[1] < -0.01:
			conservative_users.append(user[0])
		elif user[1] > 0.3:
			liberal_users.append(user[0])
		else:
			neutral_users.append(user[0])
			
	print("cons users ", len(conservative_users))
	print("lib users ", len(liberal_users))
	print("neu users ", len(neutral_users))


	liberal_tags = test_hashtag_bias_bubble.define_hashtag_bias(user_hash_dict, liberal_users)
	conservative_tags = test_hashtag_bias_bubble.define_hashtag_bias(user_hash_dict, conservative_users)
	neutral_tags = test_hashtag_bias_bubble.define_hashtag_bias(user_hash_dict, neutral_users)
	non_url_tags = test_hashtag_bias_bubble.define_hashtag_bias(user_hash_dict, non_url_users)

	liberal_unique = test_hashtag_bias_bubble.unique_tags(liberal_tags)
	conservative_unique = test_hashtag_bias_bubble.unique_tags(conservative_tags)
	neutral_unique = test_hashtag_bias_bubble.unique_tags(neutral_tags)

	#associate screen names and user id's with bias
	ids_and_sn =[[str(u),sn] for u,sn in zip(user_id_list,user_sn_list)]

	conservative_screen_names = test_hashtag_bias_bubble.potential_bias(ids_and_sn, conservative_users)
	liberal_screen_names = test_hashtag_bias_bubble.potential_bias(ids_and_sn, liberal_users)
	neutral_screen_names = test_hashtag_bias_bubble.potential_bias(ids_and_sn, neutral_users)
	non_url_user_screen_names = test_hashtag_bias_bubble.potential_bias(ids_and_sn, non_url_users)

	maybe_conservative_retweet_bias = test_hashtag_bias_bubble.potential_bias_based_on_retweets(reply_to_sn_dict, non_url_users, conservative_screen_names)
	maybe_liberal_retweet_bias = test_hashtag_bias_bubble.potential_bias_based_on_retweets(reply_to_sn_dict, non_url_users, liberal_screen_names)
	maybe_neutral_retweet_bias = test_hashtag_bias_bubble.potential_bias_based_on_retweets(reply_to_sn_dict, non_url_users, neutral_screen_names)

	liberal_hash_users = test_hashtag_bias_bubble.non_url_user_hash(user_hash_dict, non_url_users, liberal_unique)
	conservative_hash_users = test_hashtag_bias_bubble.non_url_user_hash(user_hash_dict, non_url_users, conservative_unique)
	neutral_hash_users = test_hashtag_bias_bubble.non_url_user_hash(user_hash_dict, non_url_users, neutral_unique)

	#match hashtag bias with sources bias and try to confirm source bias- are they the same?
	liberal_results = test_hashtag_bias_bubble.positive_and_negative_results(liberal_hash_users, maybe_liberal_retweet_bias)
	conservative_results = test_hashtag_bias_bubble.positive_and_negative_results(conservative_hash_users, maybe_conservative_retweet_bias)
	neutral_results = test_hashtag_bias_bubble.positive_and_negative_results(neutral_hash_users, maybe_neutral_retweet_bias)

def create_retweet_user_dict(user_id_list, all_users_full_tweets_dict):
	#create a dict with reply_to screen names and user id's 
	#users that tweeted at other users

	count = 0

	reply_to_sn_dict = {}

	for user in user_id_list:
		
		if user not in reply_to_sn_dict:
			reply_to_sn_dict[user] = []
		
		for doc in all_users_full_tweets_dict[user]:
			reply_to_sn_dict[user].append(doc['in_reply_to_screen_name'])

	return reply_to_sn_dict

def create_hashtag_user_dict(user_id_list, all_users_full_tweets_dict):
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

	return user_hash_dict	

#create cooccurence matrix 
def create_cooc_matrix(data, standardize = False):
	cooc_m = np.zeros((data.shape[1], data.shape[1]))
	for i, c1 in enumerate(data.T):
		for j, c2 in enumerate(data.T):
			cooc_m[i,j] = np.sum(c1*c2)
	if standardize:
		return cooc_m / data.shape[0]
	return cooc_m

def diagonal_cooc_matrix(matrix):

	new_matrix = (matrix/np.diagonal(matrix)).T

# create matrix of user bias using pew results:
def create_bias_matrix(expanded_url_dict_with_user, news_sources):
	bias_value_return_list = []
	user_sources = []
	
	count = 0

	for user_id in expanded_url_dict_with_user:

		sources = []

		#to create array of zeros:
		user_zero_vector_bias = list(np.zeros(len(news_sources)))
		
		# what sources *did* this user use        
		url_item = expanded_url_dict_with_user[user_id]
		for item in url_item:
			o = urlparse(item)
			root_url = o.hostname
			sources.append(root_url)
			root_url_split = root_url.split(".")
			
			if root_url_split[0] == "www":
				user_sources.append(root_url_split[1])
			else:
				user_sources.append(root_url_split[0])
									  
		for i, source in enumerate(news_sources):            
			user_zero_vector_bias[i] = user_sources.count(source)
			# if source in root_url_split:
			# 	user_zero_vector_bias[i]+=1
			
		bias_value_return_list.append(user_zero_vector_bias)
		count +=1
		
	bias_value_return_list = np.array(bias_value_return_list)

	return bias_value_return_list

def pew_bias_matrix(bias_matrix):

	#multiply results by bias measure from pew
	user_bias_measure_pew = []

	for user in bias_matrix:
		user_bias_measure_pew.append(user*bias)

	# transform to matrix
	user_bias_measure_pew = np.array(user_bias_measure_pew)

	# transpose of matrix 
	user_bias_measure_pew = user_bias_measure_pew.T

	#sum columns (users) of matrix 
	i = 0

	while i < len(user_bias_measure_pew):
		
		bias_number_user = list(sum(user_bias_measure_pew))
		i+=1

	return(bias_number_user)

def user_ids_user_bias(url_users, bias_number_user):

	#associate user ID's with user bias again
	users_and_biases =[[str(u),b] for u,b in zip(url_users,bias_number_user)]

	return users_and_biases

def main():

	# define input data file
	input_data_file = '/Users/Kellie/Desktop/geotagged_tweets_20160812-0912.json'
	
	# generate data structure
	create_and_test_user_bias_matrix(input_data_file)

if __name__ == "__main__":
	main()
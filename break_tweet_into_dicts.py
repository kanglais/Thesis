import json

input_file = '/Users/Kellie/Desktop/sep_tweets.json'

all_users_terms_dict = {}

with open(input_file, 'r') as raw_data:

	all_users_full_tweets_dict = json.load(raw_data)
#list of all the user id's 
user_ids = list(all_users_full_tweets_dict.keys())

#break raw tweet dictionary into series of lists containing relevant info 
#based on user ids (so order remains the same)

def create_user_id_list(user_ids, all_users_full_tweets_dict):
	user_id_list = []

	for user in user_ids:
		for doc in all_users_full_tweets_dict[user]:
			user_id_list.append(user)

	return user_id_list

def create_user_sn_list(user_ids, all_users_full_tweets_dict):
	user_sn_list = []

	for user in user_ids:
		for doc in all_users_full_tweets_dict[user]:		
			user_sn_list.append(doc['user']['screen_name'])

	return user_sn_list

def create_user_mentions_full_list(user_ids, all_users_full_tweets_dict):
	user_mentions_full_list = []

	for user in user_ids:

		for doc in all_users_full_tweets_dict[user]:
			user_mentions_full_list.append(doc['entities']['user_mentions'])

	return user_mentions_full_list


def create_url_full_list(user_ids, all_users_full_tweets_dict):
	url_full_list = []

	for user in user_ids:
		for doc in all_users_full_tweets_dict[user]:
			url_full_list.append(doc['entities']['urls'])

	return url_full_list


def create_hashtags_list(user_ids, all_users_full_tweets_dict):
	hashtags_list = []

	for user in user_ids:
		for doc in all_users_full_tweets_dict[user]:
			hashtags_list.append(doc['entities']['hashtags'])

	return hashtags_list


def create_reply_to_sn_list(user_ids, all_users_full_tweets_dict):
	reply_to_sn_list = []

	for user in user_ids:
		for doc in all_users_full_tweets_dict[user]:
			reply_to_sn_list.append(doc['in_reply_to_screen_name'])

	return reply_to_sn_list

def create_created_at_list(user_ids, all_users_full_tweets_dict):
	created_at_list = []

	for user in user_ids:
		for doc in all_users_full_tweets_dict[user]:
			created_at_list.append(doc['created_at'])

	return created_at_list

def create_hash_mention_list(user_ids, all_users_full_tweets_dict):
	hash_list = []
	mention_list = []

	for user in user_ids:
		for doc in all_users_full_tweets_dict[user]:

			hashtags = doc['entities']['hashtags']
			mentions = doc['entities']['user_mentions']

			for tag in hashtags:		    
				hash_list.append(tag['text'])

			for mention in mentions:
				mention_list.append(mention['screen_name'])

	unique = set(hash_list + mention_list)
	return unique

def create_all_users_terms_dict(user_ids, all_users_full_tweets_dict):

	all_users_terms_dict = {}
	for user in user_ids:

		all_users_terms_dict[user] = []

		for doc in all_users_full_tweets_dict[user]:

			hashtags = doc['entities']['hashtags']
			mentions = doc['entities']['user_mentions']

			for tag in hashtags:		    
				all_users_terms_dict[user].append(tag['text'])

			for mention in mentions:
				all_users_terms_dict[user].append(mention['screen_name'])

	return all_users_terms_dict


user_id_list = create_user_id_list(user_ids, all_users_full_tweets_dict)
user_sn_list = create_user_sn_list(user_ids, all_users_full_tweets_dict)
user_mentions_full_list = create_user_mentions_full_list(user_ids, all_users_full_tweets_dict)
url_full_list = create_url_full_list(user_ids, all_users_full_tweets_dict)
hashtags_list = create_hashtags_list(user_ids, all_users_full_tweets_dict)
reply_to_sn_list = create_reply_to_sn_list(user_ids, all_users_full_tweets_dict)
created_at_list = create_created_at_list(user_ids, all_users_full_tweets_dict)
hash_mention_list = create_hash_mention_list(user_ids, all_users_full_tweets_dict)
all_users_terms_dict = create_all_users_terms_dict(user_ids, all_users_full_tweets_dict)

# print(user_id_list)
# print(user_sn_list)
# print(user_mentions_full_list)
# print(url_full_list)
# print(hashtags_list)
# print(reply_to_sn_list)
# print(created_at_list)
# print(hash_mention_list) 
#print(all_users_terms_dict)

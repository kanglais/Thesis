import test_user_bias_bubble


#get most frequently used hashtags in whole set

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


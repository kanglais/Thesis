import numpy as np 
import json
from collections import defaultdict
from urllib.parse import urlparse
from collections import Counter
import pprint
import pandas as pd

input_data_file = './data/only_urls copy.json'

with open(input_data_file, 'rb') as raw_url_data:

    all_users_url_dict = json.load(raw_url_data)

users_and_bias_measure = []

for users in all_users_url_dict:

    user_bias = []

    url_item = all_users_url_dict[users]
    for item in url_item:
        o = urlparse(item)
        root_url = o.hostname

        # for url in root_url: 
        if 'breitbart' in root_url: 
            bias = 0.6
            user_bias.append(bias)
        elif 'limbaugh' in root_url:
            bias = 0.6
            user_bias.append(bias)
        elif 'theblaze' in root_url:
            bias = 0.6
            user_bias.append(bias)
        elif 'hannity' in root_url:
            bias = 0.6
            user_bias.append(bias)
        elif 'glenbeck' in root_url:
            bias = 0.6
            user_bias.append(bias)
        elif 'drudge report' in root_url:
            bias = 0.5
            user_bias.append(bias)
        elif 'fox' in root_url: 
            bias = 0.2
            user_bias.append(bias)
        elif 'wallstreetjournal' in root_url:
            bias = -0.1
            user_bias.append(bias)
        elif 'yahoo' in root_url:
            bias = -0.1
            user_bias.append(bias)
        elif 'usatoday' in root_url:
            bias = -0.1
            user_bias.append(bias)
        elif 'abc' in root_url:
            bias = -0.1
            user_bias.append(bias)
        elif 'bloomberg' in root_url:
            bias = -0.1
            user_bias.append(bias)
        elif 'google' in root_url:
            bias = -0.1
            user_bias.append(bias)
        elif 'cbs' in root_url:
            bias = -0.1
            user_bias.append(bias)
        elif 'nbc' in root_url:
            bias = -0.2
            user_bias.append(bias)
        elif 'cnn' in root_url:
            bias = -0.2
            user_bias.append(bias)
        elif 'msnbc' in root_url:
            bias = -0.3
            user_bias.append(bias)
        elif 'buzzfeed' in root_url:
            bias = -0.4
            user_bias.append(bias)
        elif 'pbs' in root_url:
            bias = -0.4
            user_bias.append(bias)
        elif 'bbc' in root_url:
            bias = -0.4
            user_bias.append(bias)
        elif 'huffingtonpost' in root_url:
            bias = -0.4
            user_bias.append(bias)
        elif 'washingtonpost' in root_url:
            bias = -0.4
            user_bias.append(bias)
        elif 'economist' in root_url:
            bias = -0.4
            user_bias.append(bias)
        elif 'politico' in root_url:
            bias = -0.4
            user_bias.append(bias)
        elif 'dailyshow' in root_url: 
            bias = -0.5
            user_bias.append(bias)
        elif 'guardian' in root_url: 
            bias = -0.5
            user_bias.append(bias)
        elif 'aljazeera' in root_url: 
            bias = -0.5
            user_bias.append(bias)
        elif 'npr' in root_url: 
            bias = -0.5
            user_bias.append(bias)
        elif 'colbertreport' in root_url: 
            bias = -0.5
            user_bias.append(bias)
        elif 'nytimes' in root_url: 
            bias = -0.5
            user_bias.append(bias)
        elif 'slate' in root_url:
            bias = -0.6
            user_bias.append(bias)
        elif 'newyorker' in root_url:
            bias = -0.6
            user_bias.append(bias)
        else: 
            bias = 0
            user_bias.append(bias)
    if len(user_bias)==0:
        users_and_bias_measure.append([users, 0])
    else:
        users_and_bias_measure.append([users, (np.mean(user_bias))])

#pprint.pprint(users_and_bias_measure)

pd.pivot_table(all_users_url_dict, index=users_and_bias_measure[users], columns=users_and_bias_measure[users])
# import matplotlib.pylab as plt


# for item in users_and_bias_measure:
    
#     x = item[1]
#     y = np.power(x, 2) 

#     plt.errorbar(x, y, linestyle='None', marker='^')

# plt.savefig('./data/url_bias.png')
# #plt.show()



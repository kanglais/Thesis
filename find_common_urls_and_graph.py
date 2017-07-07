import numpy as np 
from numpy import *

from collections import defaultdict

freqs = Counter(root_urls)
#print(freqs)

most_common_urls = (defaultdict(list))

for word, count in freqs.most_common(100):
    most_common_urls[word].append(count)
    for url in most_common_urls: 
        if 'breitbart' in url: 
            bias = 0.6
            most_common_urls[url].append(bias)
        elif 'limbaugh' in url:
            bias = 0.6
            most_common_urls[url].append(bias)
        elif 'theblaze' in url:
            bias = 0.6
            most_common_urls[url].append(bias)
        elif 'hannity' in url:
            bias = 0.6
            most_common_urls[url].append(bias)
        elif 'glenbeck' in url:
            bias = 0.6
            most_common_urls[url].append(bias)
        elif 'drudge report' in url:
            bias = 0.5
            most_common_urls[url].append(bias)
        elif 'fox' in url: 
            bias = 0.2
            most_common_urls[url].append(bias)
        elif 'wallstreetjournal' in url:
            bias = -0.1
            most_common_urls[url].append(bias)
        elif 'yahoo' in url:
            bias = -0.1
            most_common_urls[url].append(bias)
        elif 'usatoday' in url:
            bias = -0.1
            most_common_urls[url].append(bias)
        elif 'abc' in url:
            bias = -0.1
            most_common_urls[url].append(bias)
        elif 'bloomberg' in url:
            bias = -0.1
            most_common_urls[url].append(bias)
        elif 'google' in url:
            bias = -0.1
            most_common_urls[url].append(bias)
        elif 'cbs' in url:
            bias = -0.1
            most_common_urls[url].append(bias)
        elif 'nbc' in url:
            bias = -0.2
            most_common_urls[url].append(bias)
        elif 'cnn' in url:
            bias = -0.2
            most_common_urls[url].append(bias)
        elif 'msnbc' in url:
            bias = -0.3
            most_common_urls[url].append(bias)
        elif 'buzzfeed' in url:
            bias = -0.4
            most_common_urls[url].append(bias)
        elif 'pbs' in url:
            bias = -0.4
            most_common_urls[url].append(bias)
        elif 'bbc' in url:
            bias = -0.4
            most_common_urls[url].append(bias)
        elif 'huffingtonpost' in url:
            bias = -0.4
            most_common_urls[url].append(bias)
        elif 'washingtonpost' in url:
            bias = -0.4
            most_common_urls[url].append(bias)
        elif 'economist' in url:
            bias = -0.4
            most_common_urls[url].append(bias)
        elif 'politico' in url:
            bias = -0.4
            most_common_urls[url].append(bias)
        elif 'dailyshow' in url: 
            bias = -0.5
            most_common_urls[url].append(bias)
        elif 'guardian' in url: 
            bias = -0.5
            most_common_urls[url].append(bias)
        elif 'aljazeera' in url: 
            bias = -0.5
            most_common_urls[url].append(bias)
        elif 'npr' in url: 
            bias = -0.5
            most_common_urls[url].append(bias)
        elif 'colbertreport' in url: 
            bias = -0.5
            most_common_urls[url].append(bias)
        elif 'nytimes' in url: 
            bias = -0.5
            most_common_urls[url].append(bias)
        elif 'slate' in url:
            bias = -0.6
            most_common_urls[url].append(bias)
        elif 'newyorker' in url:
            bias = -0.6
            most_common_urls[url].append(bias)
        else: 
            bias = 0
            most_common_urls[url].append(bias)


import matplotlib.pylab as plt


for item in most_common_urls.items():
    label = item[0]
    data = item[1]
    for i in data: 
        x = data[0]
        y = data[1]
        plt.scatter(x, y, color='blue', marker='*')
        
plt.xlabel('Frequency of Tweets')
plt.ylabel('Bias: Conservative to Liberal')


plt.show()

for item in most_common_urls.items():
    label = item[0]
    data = item[1]
    for i in data:
        if data[1]>0: 
            x = data[0]
            y = data[1]
            plt.scatter(x, y, color='blue', marker='*')
        plt.annotate(label, xy = (x, y))
        
plt.xlabel('Frequency of Tweets')
plt.ylabel('Bias: Conservative')
plt.title('Conservative Tweets')


plt.show()

for item in most_common_urls.items():
    label = item[0]
    data = item[1]
    for i in data:
        if data[1]<0: 
            x = data[0]
            y = data[1]
            plt.scatter(x, y, color='blue', marker='*')
    plt.annotate(label, xy = (x, y))
        
plt.xlabel('Frequency of Tweets')
plt.ylabel('Bias: Liberal')
plt.title('Liberal Tweets')


plt.show()

for item in most_common_urls.items():
    label = item[0]
    data = item[1]
    for i in data:
        #excludes twitter bc there are too many links // messes w graph
        if data[1]==0 and data[0]<40000: 
            x = data[1]
            y = data[0]
            plt.scatter(x, y, color='blue', marker='*')
    plt.annotate(label, xy = (x, y))
        
plt.xlabel('Frequency of Tweets')
plt.ylabel('Bias = 0')
plt.title('UnBiased Tweets')


plt.show()

from collections import Counter

hashtags = []

for doc in collection.find({'hashtags': {'$exists' : 'true'}}):
    hashtags.append(doc['hashtags'])

#print(collection.find({'hashtags': {'$exists' : 'true'}}).count())
print(hashtags)


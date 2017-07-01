import tweepy
from tweepy import OAuthHandler
import json
import re
import operator
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string
import csv

#nltk.download('stopwords')

consumer_key = 'wIjR8kT4GDPcReutoPvtaZKs3'
consumer_secret = 'xKZRQzu35WwmMIigHh2G9M9VHBgqdEQlSaPugebWCSprpPDszC'
access_token = '829641247962836993-kbbUiL3mCfOic2XHDp0fJ2OtIzVrDVJ'
access_secret = 'Td6gHrNB6FnUtjySKqmm59fSkOHL33ggVsQ41dQPvssEh'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

S_DIR = "/Users/Kellie/Desktop/thesis"

tweets = []

with open('/Users/Kellie/Desktop/thesis/geotagged_tweets_20160812-0912.json', 'r') as f:
	line = f.readline()
	tweet = json.loads(line)
	tweets.append(json.loads(line))
	#print(json.dumps(tweet, indent=4))

#below from marco bonanzi tutorial

emoticons_str = r"""
	(?:
		[:=;] # eyes
		[oO\-]? # nose (optional)
		[D\)\]\(\]/\\OpP] # mouth
	)"""

regex_str = [ # list of possible patterns
	emoticons_str, 
	r'<[^>]+>', # html tags
	r'(?:@[\w_]+)', # @ mentions
	r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash tags
	#r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


with open('/Users/Kellie/Desktop/thesis/geotagged_tweets_20160812-0912.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        #print(json.dumps(tweet, indent=4))

hashtags = ['#donaldtrump', '#trumppence16', '#crookedhillary', '#hillaryclinton', '#trump', '#nevertrump', '#imwithher',
'#dumptrump','#hillaryclinton', '#imwithher', '#crookedhillary', '#maga', '#trump', '#trumppence16', '#nevertrump', '#hillary', '#neverhillary','@realDonaldTrump', '@HillaryClinton']

hashtags = list(set(hashtags))

fname = '/Users/Kellie/Desktop/thesis/geotagged_tweets_20160812-0912.json'

punctuation = list(string.punctuation)

stop = stopwords.words('english') + punctuation + ['rt', 'via']

#if has url
		#terms_url = [term for term in preprocess(tweet['text'])
		#s	if term.startswith(('http', 'https', '?://', '(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'))]

with open(fname, 'r') as f:
	count_all = Counter()
	for line in f: 
		tweet = json.loads(line)
		#create a list with all the terms
		#terms_all = [term for term in preprocess(tweet['text'])]
		#terms w/ stopwords removed
		terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
		#count terms only once, equivalent to Document Frequency
		#terms_single = set(terms_all)
		#count hashtags only
		terms_hash = [term for term in preprocess(tweet['text'])
			if term in hashtags]
		#count terms only (no hashtags, no mentions)
		terms_only = [term for term in preprocess(tweet['text'])
			if term not in stop and
			not term.startswith(('#', '@', 'amp'))]
		#update the counter
		count_all.update(terms_stop)
	#print most frequent
	#print(count_all.most_common(10))

def only_relevant(tweet):
    relevant = {}
    relevant['screen_name'] = tweet['user']['screen_name']
    relevant['text'] = tweet['text']
    relevant['timestamp'] = tweet['timestamp_ms']
    relevant['following'] = tweet['user']['friends_count']
    relevant['followers'] = tweet['user']['followers_count']
    relevant['description'] = tweet['user']['description']
    relevant['user_location'] = tweet['user']['location']
    relevant['in_reply_to_screen_name'] = tweet['in_reply_to_screen_name']
    relevant['user_mentions'] = tweet['entities']['user_mentions']
    relevant['hashtags'] = tweet['entities']['hashtags']
    relevant['url'] = tweet['entities']['urls']
    
    return relevant

with open(fname, 'r') as f: 
	for line in f:
		tweet = json.loads(line)
		print(only_relevant(tweet))

with open()
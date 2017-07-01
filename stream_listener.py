import os
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

D_DIR = "/Users/Kellie/Desktop/fundDS/output"
#K_DIR = ""
TWEETS_FILE = open("tweets_file.txt", 'w')
ERROR_FILE = open("error_file.txt", 'w')

consumer_key = 'wIjR8kT4GDPcReutoPvtaZKs3'

consumer_secret = 'xKZRQzu35WwmMIigHh2G9M9VHBgqdEQlSaPugebWCSprpPDszC'

access_token = '829641247962836993-kbbUiL3mCfOic2XHDp0fJ2OtIzVrDVJ'

access_secret = 'Td6gHrNB6FnUtjySKqmm59fSkOHL33ggVsQ41dQPvssEh'

class ElectionListener(StreamListener):
    def on_data(self, data):
        try:
            with open(os.path.join(D_DIR, TWEETS_FILE), 'a') as f:
                f.write(data)
        except BaseException as e:
            print('Error on_data: %s' % str(e))
            with open(os.path.join(D_DIR, ERROR_FILE), 'a') as f:
                f.write('Error on_data: %s\n' % str(e))
        return True

def on_error(self, status):
    print(status)
    with open(os.path.join(D_DIR, ERROR_FILE), 'a') as f:
        f.write('Error stream: %s\n' % str(status))
    return True

with open(os.path.join(K_DIR, 'consumer_key'), 'r') as rf:
    consumer_key = rf.read().strip()
with open(os.path.join(K_DIR, 'consumer_secret'), 'r') as rf:
    consumer_secret = rf.read().strip()
with open(os.path.join(K_DIR, 'access_token'), 'r') as rf:
    access_token = rf.read().strip()
with open(os.path.join(K_DIR, 'access_secret'), 'r') as rf:
    access_secret = rf.read().strip()

hashtags = ['#donaldtrump', '#trumppence16', '#crookedhillary', '#hillaryclinton', '#trump', '#nevertrump', '#imwithher',
'#dumptrump','#hillaryclinton', '#imwithher', '#crookedhillary', '#maga', '#trump', '#trumppence16', '#nevertrump', '#hillary', '#neverhillary','@realDonaldTrump', '@HillaryClinton']

hashtags = list(set(hashtags))

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)

while True:
  try:
    twitter_stream = Stream(auth, ElectionListener())
    twitter_stream.filter(track=hashtags)
  except Exception as e:
    print('Error: %s' % str(e))
    with open(os.path.join(D_DIR, ERROR_FILE), 'a') as f:
      f.write('Error: %s\n' % str(e))
  continue





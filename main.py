{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import tweepy\n",
    "from tweepy import Stream\n",
    "from tweepy.streaming import StreamListener\n",
    "from tweepy import OAuthHandler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "D_DIR = [DIRECTORY TO STORE THE DATA]\n",
    "K_DIR = [DIRECTORY WITH THE KEYS]\n",
    "TWEETS_FILE = [FILE TO STORE THE TWEETS]\n",
    "ERROR_FILE = [STORING THE ERRORS]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class ElectionListener(StreamListener):\n",
    "    def on_data(self, data):\n",
    "        try:\n",
    "            with open(os.path.join(D_DIR, TWEETS_FILE), 'a') as f:\n",
    "                f.write(data)\n",
    "        except BaseException as e:\n",
    "            print('Error on_data: %s' % str(e))\n",
    "            with open(os.path.join(D_DIR, ERROR_FILE), 'a') as f:\n",
    "                f.write('Error on_data: %s\\n' % str(e))\n",
    "        return True\n",
    "\n",
    "def on_error(self, status):\n",
    "    print(status)\n",
    "    with open(os.path.join(D_DIR, ERROR_FILE), 'a') as f:\n",
    "        f.write('Error stream: %s\\n' % str(status))\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "with open(os.path.join(K_DIR, 'consumer_key'), 'r') as rf:\n",
    "    consumer_key = rf.read().strip()\n",
    "with open(os.path.join(K_DIR, 'consumer_secret'), 'r') as rf:\n",
    "    consumer_secret = rf.read().strip()\n",
    "with open(os.path.join(K_DIR, 'access_token'), 'r') as rf:\n",
    "    access_token = rf.read().strip()\n",
    "with open(os.path.join(K_DIR, 'access_secret'), 'r') as rf:\n",
    "    access_secret = rf.read().strip()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}

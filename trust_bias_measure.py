import test_user_bias_bubble
import numpy as np 
import json
from collections import defaultdict
from urllib.parse import urlparse
from collections import Counter
import pprint

#source: overall consistlib mostlib mixed mostcons consistcons
new_sources_and_trust = {
'cnn' :	0.66,
'abc' :	0.59,
'nbc' : 0.63,
'cbs' :	0.55,
'fox' : -0.88,
'msnbc'	: 0.52,
'pbs' :	0.71,
'bbc' :	0.69,
'nytimes' :	0.62,
'usatoday': 	0.38,
'wallstreetjournal':	0.35,
'npr' : 0.72,
'washingtonpost' : 0.48,
'google' : 0.29,
'yahoo' : 0.25,
'huffingtonpost' : 0.38,
'dailyshow' : 0.45,
'colbertreport' : 0.36,
'newyorker' : 0.32,
'economist' : 0.30,
'hannity' : -0.62,
'limbaugh' : -0.58,
'bloomberg' : 0.18,
'glennbeck' : -0.51,
'aljazeera' : 0.28,
'drudgereport' : -0.34,
'guardian' : 0.21,
'politico' : 0.21,
'theblaze' : -0.37,
'motherjones' : 0.25,
'breitbart' : -0.25,
'slate' :	0.14,
'edschultz': 0.14,
'buzzfeed' : 0.06,
'dailykos': 0.1,
'thinkprogress': 0.1}

print(new_sources_and_trust.keys())

for item in new_sources_and_trust:
	print(new_sources_and_trust[item])

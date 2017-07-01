from pymongo import MongoClient
import json
import os.path

client = MongoClient()
db = client.test
collection = db.tweets
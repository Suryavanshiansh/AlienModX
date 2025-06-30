# database/mongo.py

import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
    raise Exception("❌ MONGO_URL environment variable not set.")

client = MongoClient(MONGO_URL)
db = client["alienmodx"]

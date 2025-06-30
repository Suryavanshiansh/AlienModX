# database/warn_manager.py

from pymongo import MongoClient
from datetime import datetime

MONGO_URI = "your_mongo_connection_string"  # replace with config import
client = MongoClient(MONGO_URI)
db = client["alienmodx"]
warns = db["warns"]

# ➕ Add a warning
async def add_warn(chat_id, user_id):
    user = warns.find_one({"chat_id": chat_id, "user_id": user_id})
    if user:
        warns.update_one({"chat_id": chat_id, "user_id": user_id}, {"$inc": {"warns": 1}})
        return user["warns"] + 1
    else:
        warns.insert_one({"chat_id": chat_id, "user_id": user_id, "warns": 1})
        return 1

# 📊 Get warnings
async def get_warns(chat_id, user_id):
    user = warns.find_one({"chat_id": chat_id, "user_id": user_id})
    return user["warns"] if user else 0

# ❌ Reset warnings
async def reset_warns(chat_id, user_id):
    warns.delete_one({"chat_id": chat_id, "user_id": user_id})

# database/warn_manager.py

from .mongo import db

warns_col = db["warns"]

def add_warn(chat_id: int, user_id: int):
    warns_col.update_one(
        {"chat_id": chat_id, "user_id": user_id},
        {"$inc": {"count": 1}},
        upsert=True
    )

def get_warns(chat_id: int, user_id: int):
    user = warns_col.find_one({"chat_id": chat_id, "user_id": user_id})
    return user["count"] if user else 0

def reset_warns(chat_id: int, user_id: int):
    warns_col.delete_one({"chat_id": chat_id, "user_id": user_id})

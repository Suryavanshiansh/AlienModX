# database/locks.py

from .mongo import db

locks_col = db["locks"]

def lock_feature(chat_id: int, feature: str):
    locks_col.update_one(
        {"chat_id": chat_id},
        {"$addToSet": {"locked": feature}},
        upsert=True
    )

def unlock_feature(chat_id: int, feature: str):
    locks_col.update_one(
        {"chat_id": chat_id},
        {"$pull": {"locked": feature}},
        upsert=True
    )

def get_locked_features(chat_id: int):
    data = locks_col.find_one({"chat_id": chat_id})
    return data.get("locked", []) if data else []

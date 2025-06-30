# database/word_manager.py

from .mongo import db

badwords_col = db["badwords"]
flood_col = db["floodwords"]

def add_word(chat_id: int, word: str, word_type: str):
    col = badwords_col if word_type == "bad" else flood_col
    if not col.find_one({"chat_id": chat_id, "word": word}):
        col.insert_one({"chat_id": chat_id, "word": word})

def remove_word(chat_id: int, word: str, word_type: str):
    col = badwords_col if word_type == "bad" else flood_col
    col.delete_one({"chat_id": chat_id, "word": word})

def get_words(chat_id: int, word_type: str):
    col = badwords_col if word_type == "bad" else flood_col
    return [x["word"] for x in col.find({"chat_id": chat_id})]

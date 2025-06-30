# 📁 filters/utils/word_manager.py
import json
import os

# 📂 Path to word database
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)
BANWORDS_PATH = os.path.join(data_dir, "banned_words.json")

# ✅ Load banned words from JSON
def load_banned_words():
    if not os.path.exists(BANWORDS_PATH):
        with open(BANWORDS_PATH, "w") as f:
            json.dump({}, f)
    with open(BANWORDS_PATH, "r") as f:
        return json.load(f)

# 💾 Save banned words to JSON
def save_banned_words(data):
    with open(BANWORDS_PATH, "w") as f:
        json.dump(data, f, indent=2)

# ➕ Add a banned word to a group
def add_word(chat_id: int, word: str):
    words = load_banned_words()
    chat_id = str(chat_id)
    words.setdefault(chat_id, [])
    if word not in words[chat_id]:
        words[chat_id].append(word)
        save_banned_words(words)
        return True
    return False

# ❌ Remove a banned word from a group
def remove_word(chat_id: int, word: str):
    words = load_banned_words()
    chat_id = str(chat_id)
    if chat_id in words and word in words[chat_id]:
        words[chat_id].remove(word)
        save_banned_words(words)
        return True
    return False

# 📜 Get all banned words for a group
def get_words(chat_id: int):
    words = load_banned_words()
    return words.get(str(chat_id), [])

# 🔍 Check if text contains banned word
def contains_banned_word(chat_id: int, text: str):
    banned = get_words(chat_id)
    text = text.lower()
    return any(word.lower() in text for word in banned)


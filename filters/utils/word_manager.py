# filters/utils/word_manager.py

import re

# 🛑 Detect banned words from list
def contains_banned_word(text: str, banned_words: list) -> bool:
    for word in banned_words:
        if re.search(rf"\b{re.escape(word)}\b", text, re.IGNORECASE):
            return True
    return False

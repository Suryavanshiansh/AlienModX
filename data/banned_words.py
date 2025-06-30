# 🚫 List of globally banned words
BANNED_WORDS = [
    "badword1",
    "badword2",
    "offensiveword",
    "slur1",
    "slur2"
]

def is_banned_word(text: str) -> bool:
    """Check if any banned word is in the given text."""
    text = text.lower()
    return any(word in text for word in BANNED_WORDS)


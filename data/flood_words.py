# 🌊 Trigger words or spammy patterns for flood detection
FLOOD_TRIGGERS = [
    "buy now",
    "free followers",
    "click here",
    "visit my profile",
    "🔥🔥🔥"
]

def is_flood_message(text: str) -> bool:
    """Detect if a message looks spammy/flood-like."""
    text = text.lower()
    return any(trigger in text for trigger in FLOOD_TRIGGERS)


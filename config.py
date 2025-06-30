# ⚙️ config.py - Configuration for Auto Moderation Rental Bot
import os
from dotenv import load_dotenv

# 🔄 Load environment variables from .env if present
load_dotenv()

# 🔐 API Credentials
API_ID = int(os.getenv("API_ID", 12345))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
SESSION_NAME = os.getenv("SESSION_NAME", "RentalModBot")

# 👑 Owner and Logging Configurations
OWNER_ID = int(os.getenv("OWNER_ID", 123456789))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", -1001234567890))

# 🛡️ Default Settings
DEFAULT_PREFIX = os.getenv("DEFAULT_PREFIX", "!")
BANNED_WORDS_FILE = "filters/data/banned_words.json"
FOOD_DATA_FILE = "filters/data/foood_data.json"

# ✅ Configuration Loaded
print("⚙️ Configurations loaded successfully!")


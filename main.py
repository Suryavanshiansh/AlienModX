import asyncio
import logging
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from database.mongo import connect_to_mongo

# 🛠️ Colorful Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="\033[1;32m[%(levelname)s]\033[0m %(message)s"
)
logger = logging.getLogger("💎 AlienModX")

# 🚀 Pyrogram Client with Plugin Autoload
app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"}
)

# 🧠 Main entry point
async def main():
    # 📡 Connect to MongoDB
    await connect_to_mongo()

    # ✅ Start the bot
    await app.start()
    me = await app.get_me()
    logger.info(f"🤖 Bot @{me.username} started successfully!")

    # 💤 Wait for idle
    await idle()

    # ❎ Stop the bot
    await app.stop()
    logger.info("👋 Bot stopped gracefully!")

# 🧩 Run the bot
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("⚠️ Bot interrupted manually.")

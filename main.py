import asyncio
import logging
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME

# 🛠️ Setup Colorful Logging
logging.basicConfig(
    level=logging.INFO,
    format="\033[1;32m[%(levelname)s]\033[0m %(message)s"
)
logger = logging.getLogger("💎 ALienModX")

# 🤖 Bot Client with Plugin Magic
app = Client(
    name=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# 🚦 Entry Function
async def main():
    try:
        await app.start()
        logger.info("🎯 Bot is online and moderating like a boss!")
        await idle()
    except Exception as e:
        logger.error(f"❌ Bot crashed with error: {e}")
    finally:
        await app.stop()
        logger.info("👋 Bot session ended. Peace out!")

# 🧠 Start the Show
if __name__ == "__main__":
    asyncio.run(main())

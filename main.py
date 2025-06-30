import asyncio
import logging
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME

# 🛠️ Setup Colorful Logging
logging.basicConfig(
    level=logging.INFO,
    format="\033[1;32m[%(levelname)s]\033[0m %(message)s"
)
logger = logging.getLogger("💎 SupremeRentalBot")

# 🤖 Bot Client with Plugin Magic
app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"}
)

# 🚦 Entry Function with Swag
async def main():
    await app.start()
    logger.info("🎯 Bot is online and moderating like a boss!")
    await idle()
    await app.stop()
    logger.info("👋 Bot session ended. Peace out!")

# 🧠 Start the Show
if __name__ == "__main__":
    asyncio.run(main())

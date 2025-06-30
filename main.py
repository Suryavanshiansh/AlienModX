# 🚀 main.py - Auto Moderation Rental Bot
import asyncio
import logging
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME

# 🔧 Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("🔥 RentalBot")

# 🤖 Bot Client Setup
app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"}
)

# 🌀 Main Function
async def main():
    await app.start()
    logger.info("✅ Bot has started and is ready to rock!")
    await idle()
    await app.stop()
    logger.info("🛑 Bot has been stopped. Goodbye!")

# 🧠 Entry Point
if __name__ == "__main__":
    asyncio.run(main())


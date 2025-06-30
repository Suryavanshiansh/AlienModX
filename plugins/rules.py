from pyrogram import Client, filters
from pyrogram.types import Message

RULES = """
📜 Group Rules:
1. Be respectful
2. No links/spam
3. Follow admin instructions
"""

@Client.on_message(filters.command("rules"))
async def show_rules(client: Client, message: Message):
    await message.reply(RULES.strip())


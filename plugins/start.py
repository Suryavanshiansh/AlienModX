from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_msg(client: Client, message: Message):
    await message.reply("👋 Hello! I’m AlienModX. Type /help to get started.")

@Client.on_message(filters.command("help"))
async def help_msg(client: Client, message: Message):
    text = """
🛠️ Commands:
/addbad, /removebad, /badwords
/addflood, /removeflood, /floodwords
/ban, /kick, /mute, /unmute
/lock, /unlock
/warn, /resetwarns
/rules, /schedule, /verify
"""
    await message.reply(text.strip())

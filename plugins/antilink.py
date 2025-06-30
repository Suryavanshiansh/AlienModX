from pyrogram import Client, filters
from pyrogram.types import Message
import re

antilink_enabled = {}  # {chat_id: True/False}

@Client.on_message(filters.command("antilink") & filters.group)
async def toggle_antilink(client, message: Message):
    if not message.from_user:
        return

    if message.command[1].lower() == "on":
        antilink_enabled[message.chat.id] = True
        await message.reply("🔒 Antilink enabled.")
    elif message.command[1].lower() == "off":
        antilink_enabled[message.chat.id] = False
        await message.reply("🔓 Antilink disabled.")
    else:
        await message.reply("Usage: /antilink [on/off]")

@Client.on_message(filters.text & filters.group)
async def check_links(client, message: Message):
    if not antilink_enabled.get(message.chat.id):
        return

    if re.search(r"(t\.me|https?://)", message.text):
        try:
            await message.delete()
        except:
            pass


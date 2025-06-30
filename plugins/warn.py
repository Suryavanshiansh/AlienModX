from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID

# In-memory warn tracking (use database for production)
warn_db = {}

WARN_LIMIT = 3

@Client.on_message(filters.command("warn") & filters.group)
async def warn_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("⚠️ Reply to a user's message to warn them.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    key = f"{chat_id}:{user_id}"
    warn_db[key] = warn_db.get(key, 0) + 1
    warns = warn_db[key]

    if warns >= WARN_LIMIT:
        await message.chat.ban_member(user_id)
        warn_db[key] = 0
        await message.reply(f"❌ User banned after {WARN_LIMIT} warnings.")
    else:
        await message.reply(f"⚠️ Warning {warns}/{WARN_LIMIT} issued.")

@Client.on_message(filters.command("resetwarns") & filters.group)
async def reset_warns(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("🔁 Reply to a user to reset their warnings.")
    
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    key = f"{chat_id}:{user_id}"
    warn_db[key] = 0
    await message.reply("✅ Warnings reset.")


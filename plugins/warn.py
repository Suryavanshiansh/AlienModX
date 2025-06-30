from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import timedelta

# In-memory warn tracking (use a database for production)
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
        try:
            await client.restrict_chat_member(
                chat_id,
                user_id,
                permissions=message.chat.permissions,  # Apply default permissions = mute
                until_date=timedelta(minutes=30)
            )
            await message.reply(f"🔇 User muted for 30 minutes after {WARN_LIMIT} warnings.")
        except Exception as e:
            await message.reply(f"❌ Could not mute the user: {e}")
    else:
        await message.reply(f"⚠️ Warning {warns}/{WARN_LIMIT} issued.")

@Client.on_message(filters.command("resetwarns") & filters.group & filters.user)
async def reset_warns(client, message: Message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not (member.status in ("administrator", "creator")):
        return await message.reply("❌ Only admins or the group owner can reset warnings.")

    if not message.reply_to_message:
        return await message.reply("🔁 Reply to a user to reset their warnings.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    key = f"{chat_id}:{user_id}"
    warn_db[key] = 0
    await message.reply("✅ Warnings reset.")

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to ban them.")

    user_id = message.reply_to_message.from_user.id
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply("🚫 User has been banned manually by admin.")
    except Exception as e:
        await message.reply(f"❌ Failed to ban user: {e}")


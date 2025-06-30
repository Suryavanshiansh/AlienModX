from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from config import OWNER_ID
from filters.utils.admin_check import is_admin
from database.mongo import reset_warns_db  # New MongoDB warn reset handler

# ✅ Only Admins & Owner Allowed Decorator
def admin_only():
    return filters.group & (filters.user(OWNER_ID) | filters.create(is_admin))

# ✅ /ban Command
@Client.on_message(filters.command("ban") & admin_only())
async def ban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to ban them.")
    try:
        await message.chat.ban_member(message.reply_to_message.from_user.id)
        await message.reply("✅ User banned.")
    except Exception as e:
        await message.reply(f"❌ Failed to ban: {e}")

# ✅ /kick Command
@Client.on_message(filters.command("kick") & admin_only())
async def kick_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to kick them.")
    try:
        user_id = message.reply_to_message.from_user.id
        await message.chat.ban_member(user_id)
        await message.chat.unban_member(user_id)
        await message.reply("✅ User kicked.")
    except Exception as e:
        await message.reply(f"❌ Failed to kick: {e}")

# ✅ /mute Command
@Client.on_message(filters.command("mute") & admin_only())
async def mute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to mute them.")
    try:
        await message.chat.restrict_member(
            message.reply_to_message.from_user.id,
            permissions=ChatPermissions()
        )
        await message.reply("🔇 User muted.")
    except Exception as e:
        await message.reply(f"❌ Failed to mute: {e}")

# ✅ /unmute Command
@Client.on_message(filters.command("unmute") & admin_only())
async def unmute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to unmute them.")
    try:
        await message.chat.restrict_member(
            message.reply_to_message.from_user.id,
            permissions=ChatPermissions(can_send_messages=True, can_send_media_messages=True)
        )
        await message.reply("🔊 User unmuted.")
    except Exception as e:
        await message.reply(f"❌ Failed to unmute: {e}")

# ✅ /gban Command (example use only - you must manage database for real global ban)
@Client.on_message(filters.command("gban") & filters.user(OWNER_ID))
async def gban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to globally ban them.")
    # Just simulate for now
    await message.reply("🚫 GBan not implemented with database yet.")

# ✅ /lock All messages
@Client.on_message(filters.command("lock") & admin_only())
async def lock_group(client, message: Message):
    try:
        await message.chat.set_permissions(ChatPermissions())
        await message.reply("🔒 Group locked.")
    except Exception as e:
        await message.reply(f"❌ Failed to lock group: {e}")

# ✅ /unlock All messages
@Client.on_message(filters.command("unlock") & admin_only())
async def unlock_group(client, message: Message):
    try:
        await message.chat.set_permissions(ChatPermissions(can_send_messages=True, can_send_media_messages=True))
        await message.reply("🔓 Group unlocked.")
    except Exception as e:
        await message.reply(f"❌ Failed to unlock group: {e}")

# ✅ /resetwarns (Only Admins)
@Client.on_message(filters.command("resetwarns") & admin_only())
async def reset_warns(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to the user whose warnings you want to reset.")
    try:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        await reset_warns_db(chat_id, user_id)
        await message.reply("⚠️ Warns reset for user.")
    except Exception as e:
        await message.reply(f"❌ Failed to reset warns: {e}")


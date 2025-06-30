from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from filters.utils.admin_check import is_admin
from database.warn_manager import add_warn, reset_warns
from datetime import datetime, timedelta
from config import OWNER_ID

# ✔️ Admin-only filter (group + admin or owner)
admin_filter = filters.group & (filters.create(is_admin) | filters.user(OWNER_ID))

@Client.on_message(filters.command("ban") & admin_filter)
async def ban_user(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to ban.")
    user = message.reply_to_message.from_user.id
    try:
        await message.chat.ban_member(user)
        await message.reply("✅ User has been banned.")
    except Exception as e:
        await message.reply(f"❌ Could not ban user: {e}")

@Client.on_message(filters.command("kick") & admin_filter)
async def kick_user(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to kick.")
    user = message.reply_to_message.from_user.id
    try:
        await message.chat.ban_member(user)
        await message.chat.unban_member(user)
        await message.reply("✅ User has been kicked.")
    except Exception as e:
        await message.reply(f"❌ Could not kick user: {e}")

@Client.on_message(filters.command("mute") & admin_filter)
async def mute_user(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to mute.")
    user = message.reply_to_message.from_user.id
    try:
        await message.chat.restrict_member(user, permissions=ChatPermissions())
        await message.reply("🔇 User has been muted.")
    except Exception as e:
        await message.reply(f"❌ Could not mute user: {e}")

@Client.on_message(filters.command("unmute") & admin_filter)
async def unmute_user(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to unmute.")
    user = message.reply_to_message.from_user.id
    try:
        await message.chat.restrict_member(
            user,
            permissions=ChatPermissions(can_send_messages=True, can_send_media_messages=True)
        )
        await message.reply("🔊 User has been unmuted.")
    except Exception as e:
        await message.reply(f"❌ Could not unmute user: {e}")

@Client.on_message(filters.command("lock") & admin_filter)
async def lock_group(client: Client, message: Message):
    try:
        await message.chat.set_permissions(ChatPermissions())
        await message.reply("🔒 Group permissions locked.")
    except Exception as e:
        await message.reply(f"❌ Failed to lock group: {e}")

@Client.on_message(filters.command("unlock") & admin_filter)
async def unlock_group(client: Client, message: Message):
    try:
        await message.chat.set_permissions(
            ChatPermissions(can_send_messages=True, can_send_media_messages=True)
        )
        await message.reply("🔓 Group permissions unlocked.")
    except Exception as e:
        await message.reply(f"❌ Failed to unlock group: {e}")

@Client.on_message(filters.command("warn") & admin_filter)
async def warn_user_cmd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to warn.")
    user = message.reply_to_message.from_user.id
    chat = message.chat.id
    count = await add_warn(chat, user)

    if count >= 3:
        until = datetime.utcnow() + timedelta(minutes=30)
        await client.restrict_chat_member(chat, user, permissions=ChatPermissions(), until_date=until)
        await message.reply("⚠️ User has received 3 warnings and is muted for 30 minutes.")
    else:
        await message.reply(f"⚠️ Warning issued. Current count: {count}/3")

@Client.on_message(filters.command("resetwarns") & admin_filter)
async def reset_warns_cmd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to reset warnings.")
    user = message.reply_to_message.from_user.id
    chat = message.chat.id
    await reset_warns(chat, user)
    await message.reply("✅ User warnings have been reset.")

@Client.on_message(filters.command("gban") & filters.user(OWNER_ID))
async def gban_user(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to global ban.")
    user = message.reply_to_message.from_user.id
    # TODO: Implement persistent gban
    await message.reply("🚫 Global ban placeholder: feature not yet implemented.")

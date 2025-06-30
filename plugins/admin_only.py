# mute.py
from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import timedelta

@Client.on_message(filters.command("mute") & filters.group)
async def mute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to mute them.")

    user_id = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(
            message.chat.id,
            user_id,
            permissions=message.chat.permissions,
            until_date=timedelta(minutes=30)
        )
        await message.reply("🔇 User has been muted for 30 minutes.")
    except Exception as e:
        await message.reply(f"❌ Error muting user: {e}")


# unmute.py
@Client.on_message(filters.command("unmute") & filters.group)
async def unmute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to unmute them.")

    user_id = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(
            message.chat.id,
            user_id,
            permissions={
                "can_send_messages": True,
                "can_send_media_messages": True,
                "can_send_other_messages": True,
                "can_add_web_page_previews": True,
            }
        )
        await message.reply("🔊 User has been unmuted.")
    except Exception as e:
        await message.reply(f"❌ Error unmuting user: {e}")


# ban.py
@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to ban them.")
    try:
        await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("🚫 User has been banned.")
    except Exception as e:
        await message.reply(f"❌ Error banning user: {e}")


# kick.py
@Client.on_message(filters.command("kick") & filters.group)
async def kick_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to kick them.")
    try:
        await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("👞 User has been kicked.")
    except Exception as e:
        await message.reply(f"❌ Error kicking user: {e}")


# lock.py
@Client.on_message(filters.command("lock") & filters.group)
async def lock_chat(client, message: Message):
    try:
        await client.set_chat_permissions(message.chat.id, permissions={})
        await message.reply("🔒 Chat has been locked.")
    except Exception as e:
        await message.reply(f"❌ Error locking chat: {e}")


# unlock.py
@Client.on_message(filters.command("unlock") & filters.group)
async def unlock_chat(client, message: Message):
    try:
        await client.set_chat_permissions(
            message.chat.id,
            permissions={
                "can_send_messages": True,
                "can_send_media_messages": True,
                "can_send_other_messages": True,
                "can_add_web_page_previews": True,
            }
        )
        await message.reply("🔓 Chat has been unlocked.")
    except Exception as e:
        await message.reply(f"❌ Error unlocking chat: {e}")


# adminlog.py
admin_log = []

@Client.on_message(filters.command("adminlog") & filters.group)
async def get_adminlog(client, message: Message):
    if not admin_log:
        return await message.reply("📝 No admin actions logged yet.")
    log_text = "\n".join(admin_log[-10:])
    await message.reply(f"📋 Last admin actions:\n{log_text}")


def log_action(text: str):
    admin_log.append(text)
    if len(admin_log) > 100:
        admin_log.pop(0)


# gban.py (example using global set, in production use a DB)
gban_list = set()

@Client.on_message(filters.command("gban"))
async def gban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user to gban them.")
    user_id = message.reply_to_message.from_user.id
    gban_list.add(user_id)
    await message.reply("🌐 User has been globally banned.")


@Client.on_message(filters.group)
async def auto_kick_gbanned(client, message: Message):
    if message.from_user and message.from_user.id in gban_list:
        try:
            await client.ban_chat_member(message.chat.id, message.from_user.id)
        except:
            pass


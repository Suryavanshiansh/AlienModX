from pyrogram import Client, filters
from pyrogram.types import Message
from filters.utils.admin_check import is_admin
from database.warn_manager import add_warn, reset_warns
from datetime import datetime, timedelta
from config import OWNER_ID

# Admin-only filter
admin_filter = filters.group & (filters.create(is_admin) | filters.user(OWNER_ID))

@Client.on_message(filters.command("warn") & admin_filter)
async def warn_user_cmd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Please reply to the user you want to warn.")
    user = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    count = await add_warn(chat_id, user)

    if count >= 3:
        until_date = datetime.utcnow() + timedelta(minutes=30)
        try:
            await client.restrict_chat_member(
                chat_id,
                user,
                permissions=ChatPermissions(),  # no permissions
                until_date=until_date
            )
            await message.reply(f"🚫 User reached 3 warnings — muted for 30 minutes.")
        except Exception as e:
            await message.reply(f"❌ Failed to mute user: {e}")
    else:
        await message.reply(f"⚠️ Warn issued. This user now has {count}/3 warnings.")

@Client.on_message(filters.command("resetwarns") & admin_filter)
async def reset_warns_cmd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Please reply to the user whose warnings you want to reset.")
    user = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    await reset_warns(chat_id, user)
    await message.reply("✅ Warnings reset for this user.")

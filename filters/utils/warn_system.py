# filters/utils/warn_system.py

from database.warn_manager import add_warn, get_warns, reset_warns
from pyrogram.types import Message, ChatPermissions
from datetime import datetime, timedelta

# ⚠️ Warn + auto-mute if needed
async def warn_user(chat_id, user_id, client, message: Message):
    count = await add_warn(chat_id, user_id)

    if count == 3:
        until_date = datetime.utcnow() + timedelta(minutes=30)
        try:
            await client.restrict_chat_member(
                chat_id,
                user_id,
                permissions=ChatPermissions(),
                until_date=until_date
            )
            await message.reply("🚫 3 warns reached. User muted for 30 minutes.")
        except Exception as e:
            await message.reply(f"❌ Mute failed: {e}")
    return count

async def get_user_warns(chat_id, user_id):
    return await get_warns(chat_id, user_id)

async def reset_user_warns(chat_id, user_id):
    return await reset_warns(chat_id, user_id)


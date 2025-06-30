# 🔐 filters/utils/admin_check.py

from pyrogram import Client
from pyrogram.types import Message

async def is_user_admin(client: Client, message: Message) -> bool:
    """Check if the message sender is an admin in the chat."""
    try:
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        return member.status in ("administrator", "creator")
    except Exception:
        return False

async def is_bot_admin(client: Client, message: Message) -> bool:
    """Check if the bot is admin in the chat."""
    try:
        bot = await client.get_chat_member(message.chat.id, "me")
        return bot.status in ("administrator", "creator")
    except Exception:
        return False


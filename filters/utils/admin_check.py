
from pyrogram.types import Message
from config import OWNER_ID

# 🔐 Admin Check Filter
async def is_admin(client, message: Message) -> bool:
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    return member.status in ("administrator", "creator") or message.from_user.id == OWNER_ID


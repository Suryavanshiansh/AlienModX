from pyrogram import Client, filters
from filters.utils.admin_check import is_admin

NSFW_WORDS = ["nsfwword1", "nsfwword2"]

@Client.on_message(filters.group & ~filters.create(is_admin))
async def anti_nsfw(client, message):
    text = message.text or ""
    if any(w in text.lower() for w in NSFW_WORDS):
        await message.delete()
        await message.reply_text("🛑 NSFW content is not allowed here.")


from pyrogram import Client, filters
from filters.utils.link_checker import contains_link
from filters.utils.admin_check import is_admin

@Client.on_message(filters.group & ~filters.create(is_admin))
async def anti_link_delete(client, message):
    if contains_link(message.text or ""):
        await message.delete()
        await message.reply_text("🚫 Links are not allowed!")

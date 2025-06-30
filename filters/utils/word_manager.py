from pyrogram import Client, filters
from pyrogram.types import Message
from filters.utils.admin_check import is_admin
from config import OWNER_ID
from database.mongo import get_words, add_word, remove_word

# 🔐 Only Admins & Owner Allowed
admin_only = filters.group & (filters.user(OWNER_ID) | filters.create(is_admin))

# 🧩 Command Prefix
@Client.on_message(filters.command("addbadword") & admin_only)
async def add_badword(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Usage: /addbadword <word>")
    word = message.command[1].lower()
    added = await add_word(message.chat.id, word, "banned_words")
    if added:
        await message.reply(f"✅ Added bad word: `{word}`")
    else:
        await message.reply("❗ Word already exists.")

@Client.on_message(filters.command("removebadword") & admin_only)
async def remove_badword(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Usage: /removebadword <word>")
    word = message.command[1].lower()
    removed = await remove_word(message.chat.id, word, "banned_words")
    if removed:
        await message.reply(f"🗑️ Removed bad word: `{word}`")
    else:
        await message.reply("❗ Word not found.")

@Client.on_message(filters.command("listbadwords") & admin_only)
async def list_badwords(client, message: Message):
    words = await get_words(message.chat.id, "banned_words")
    if not words:
        return await message.reply("✅ No bad words set.")
    await message.reply("🚫 Banned Words:\n" + ", ".join(words))

# 🔁 Flood words management
@Client.on_message(filters.command("addflood") & admin_only)
async def add_floodword(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Usage: /addflood <word>")
    word = message.command[1].lower()
    added = await add_word(message.chat.id, word, "flood_words")
    if added:
        await message.reply(f"✅ Added flood word: `{word}`")
    else:
        await message.reply("❗ Word already exists.")

@Client.on_message(filters.command("removeflood") & admin_only)
async def remove_floodword(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Usage: /removeflood <word>")
    word = message.command[1].lower()
    removed = await remove_word(message.chat.id, word, "flood_words")
    if removed:
        await message.reply(f"🗑️ Removed flood word: `{word}`")
    else:
        await message.reply("❗ Word not found.")

@Client.on_message(filters.command("listfloodwords") & admin_only)
async def list_floodwords(client, message: Message):
    words = await get_words(message.chat.id, "flood_words")
    if not words:
        return await message.reply("✅ No flood words set.")
    await message.reply("💬 Flood Trigger Words:\n" + ", ".join(words))

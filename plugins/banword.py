from pyrogram import Client, filters
from pyrogram.types import Message
from filters.utils.admin_check import is_admin
from database.word_manager import add_word, remove_word, get_words

admin_filter = filters.group & filters.create(is_admin)

@Client.on_message(filters.command("addbad") & admin_filter)
async def add_bad(client, message: Message):
    word = message.text.split(maxsplit=1)[-1].lower() if len(message.command) > 1 else None
    if not word:
        return await message.reply("⚠️ Usage: /addbad <word>")
    add_word(message.chat.id, word, "bad")
    await message.reply(f"✅ Added **{word}** to bad words.")

@Client.on_message(filters.command("removebad") & admin_filter)
async def remove_bad(client, message: Message):
    word = message.text.split(maxsplit=1)[-1].lower() if len(message.command) > 1 else None
    if not word:
        return await message.reply("⚠️ Usage: /removebad <word>")
    remove_word(message.chat.id, word, "bad")
    await message.reply(f"🗑️ Removed **{word}** from bad words.")

@Client.on_message(filters.command("badwords") & admin_filter)
async def list_bad(client, message: Message):
    words = get_words(message.chat.id, "bad")
    return await message.reply("📭 No bad words set.") if not words else await message.reply("🚫 Bad words:\n" + ", ".join(words))

# Flood words similarly
@Client.on_message(filters.command("addflood") & admin_filter)
async def add_flood(client, message: Message):
    word = message.text.split(maxsplit=1)[-1].lower() if len(message.command) > 1 else None
    if not word:
        return await message.reply("⚠️ /addflood <word>")
    add_word(message.chat.id, word, "flood")
    await message.reply(f"✅ Added **{word}** to flood words.")

@Client.on_message(filters.command("removeflood") & admin_filter)
async def remove_flood(client, message: Message):
    word = message.text.split(maxsplit=1)[-1].lower() if len(message.command) > 1 else None
    if not word:
        return await message.reply("⚠️ /removeflood <word>")
    remove_word(message.chat.id, word, "flood")
    await message.reply(f"🗑️ Removed **{word}** from flood words.")

@Client.on_message(filters.command("floodwords") & admin_filter)
async def list_flood(client, message: Message):
    words = get_words(message.chat.id, "flood")
    return await message.reply("📭 No flood words set.") if not words else await message.reply("🌊 Flood words:\n" + ", ".join(words))

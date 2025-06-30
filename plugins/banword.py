from pyrogram import Client, filters
from pyrogram.types import Message
from filters.utils.admin_check import is_admin
from database.word_manager import add_word, remove_word, get_words

# ✅ Admin-only filter
admin_filter = filters.group & filters.create(is_admin)

# ➕ Add bad word
@Client.on_message(filters.command("addbad") & admin_filter)
async def add_bad_word(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Usage: /addbad <word>")

    word = message.command[1].lower()
    add_word(message.chat.id, word, "bad")
    await message.reply(f"✅ Word '**{word}**' added to bad list.")

# ❌ Remove bad word
@Client.on_message(filters.command("removebad") & admin_filter)
async def remove_bad_word(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Usage: /removebad <word>")

    word = message.command[1].lower()
    remove_word(message.chat.id, word, "bad")
    await message.reply(f"🗑️ Word '**{word}**' removed from bad list.")

# 📋 Show all bad words
@Client.on_message(filters.command("badwords") & admin_filter)
async def list_bad_words(client, message: Message):
    words = get_words(message.chat.id, "bad")
    if not words:
        return await message.reply("📭 No bad words set yet.")
    await message.reply("🛑 Bad Words List:\n" + ", ".join(words))


# ➕ Add flood word
@Client.on_message(filters.command("addflood") & admin_filter)
async def add_flood_word(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Usage: /addflood <word>")

    word = message.command[1].lower()
    add_word(message.chat.id, word, "flood")
    await message.reply(f"✅ Word '**{word}**' added to flood list.")

# ❌ Remove flood word
@Client.on_message(filters.command("removeflood") & admin_filter)
async def remove_flood_word(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("⚠️ Usage: /removeflood <word>")

    word = message.command[1].lower()
    remove_word(message.chat.id, word, "flood")
    await message.reply(f"🗑️ Word '**{word}**' removed from flood list.")

# 📋 Show all flood words
@Client.on_message(filters.command("floodwords") & admin_filter)
async def list_flood_words(client, message: Message):
    words = get_words(message.chat.id, "flood")
    if not words:
        return await message.reply("📭 No flood words set yet.")
    await message.reply("💦 Flood Words List:\n" + ", ".join(words))

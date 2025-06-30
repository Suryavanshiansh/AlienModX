# 🚫 plugins/banword.py - Manage banned words per group
from pyrogram import Client, filters
from pyrogram.types import Message
from filters.utils.admin_check import is_user_admin
from filters.utils.word_manager import add_word, remove_word, get_words, contains_banned_word

# ➕ Add a banned word
@Client.on_message(filters.command("addword") & filters.group)
async def add_banned_word(client: Client, message: Message):
    if not await is_user_admin(client, message):
        return await message.reply("🚫 You must be an admin to add banned words.")

    if len(message.command) < 2:
        return await message.reply("❗ Usage: /addword <word>")

    word = message.command[1].strip().lower()
    if add_word(message.chat.id, word):
        await message.reply(f"✅ Added banned word: `{word}`")
    else:
        await message.reply(f"⚠️ `{word}` is already banned.")

# ❌ Remove a banned word
@Client.on_message(filters.command("delword") & filters.group)
async def remove_banned_word(client: Client, message: Message):
    if not await is_user_admin(client, message):
        return await message.reply("🚫 You must be an admin to remove banned words.")

    if len(message.command) < 2:
        return await message.reply("❗ Usage: /delword <word>")

    word = message.command[1].strip().lower()
    if remove_word(message.chat.id, word):
        await message.reply(f"🗑️ Removed banned word: `{word}`")
    else:
        await message.reply(f"❌ `{word}` was not in the banned list.")

# 📜 List banned words
@Client.on_message(filters.command("listwords") & filters.group)
async def list_banned_words(client: Client, message: Message):
    words = get_words(message.chat.id)
    if not words:
        return await message.reply("📭 No banned words set in this group.")
    wordlist = "\n".join(f"- `{w}`" for w in words)
    await message.reply(f"📃 <b>Banned Words List:</b>\n{wordlist}", parse_mode="html")

# 🛡️ Delete messages containing banned words
@Client.on_message(filters.text & filters.group & ~filters.service)
async def monitor_messages(client: Client, message: Message):
    if message.from_user and await is_user_admin(client, message):
        return  # Skip admins

    if contains_banned_word(message.chat.id, message.text):
        try:
            await message.delete()
            await message.reply(f"⚠️ Banned word detected and removed.", quote=True)
        except:
            pass


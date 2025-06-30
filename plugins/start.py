from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.first_name}!\n\n"
        "I'm ALienModX — your powerful Telegram moderator bot.\n"
        "Use /help to see available commands."
    )

@Client.on_message(filters.command("help"))
async def help_handler(client, message: Message):
    await message.reply_text(
        "🛠️ Available Commands:\n"
        "/warn - Warn a user\n"
        "/resetwarns - Reset user's warnings\n"
        "/antilink [on/off] - Enable/disable anti-link\n"
        "/ban - Ban user\n"
        "/mute - Mute user\n"
        "/kick - Kick user"
    )

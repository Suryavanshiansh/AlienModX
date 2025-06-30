from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.new_chat_members)
async def welcome_verify(client: Client, message: Message):
    new = message.new_chat_members[0]
    await message.reply(f"👋 Welcome, {new.first_name}! Please type `/verify` to verify yourself.")


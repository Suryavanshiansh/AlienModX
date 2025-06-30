from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.new_chat_members)
async def welcomes(client: Client, message: Message):
    for user in message.new_chat_members:
        await message.reply(f"👋 Welcome to the group, {user.first_name}!")


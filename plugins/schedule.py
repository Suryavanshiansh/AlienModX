from pyrogram import Client, filters
from datetime import datetime

@Client.on_message(filters.command("schedule"))
async def schedule_msg(client: Client, message: Message):
    await message.reply(f"📅 Server time is {datetime.now():%Y-%m-%d %H:%M:%S}")


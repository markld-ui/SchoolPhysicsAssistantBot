import logging

from aiogram import Bot

from data.config import ADMINS, TOKEN

async def notify_admin():
    for admin in ADMINS:  # We go through the list of admins and at each iteration we write in a private message about the launch of the bot
        try:
            await Bot(token=TOKEN, parse_mode="HTML").send_message(text="Bot online", chat_id=admin)
        except Exception as err:
            logging.exception(err)

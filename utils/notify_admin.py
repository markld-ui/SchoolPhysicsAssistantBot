import logging

from loader import dp
from data.config import ADMINS

async def notify_admin(dp):
    for admin in ADMINS:  # We go through the list of admins and at each iteration we write in a private message about the launch of the bot
        try:
            await dp.bot.send_message(text="Bot online", chat_id=admin)
        except Exception as err:
            logging.exception(err)

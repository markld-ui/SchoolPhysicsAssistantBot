import handlers

import asyncio
from loader import bot
from utils.notify_admin import notify_admin
#from utils.set_commands import set_commands

from loader import dp


async def start_bot_info(dp):
    '''function calls other functions to load initial commands and settings for the admin'''
    #await set_commands(bot)
    await notify_admin()

    try:
        await dp.start_polling(bot)
    finally:
        bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(start_bot_info(dp))
    except KeyboardInterrupt:
        print('Exit')
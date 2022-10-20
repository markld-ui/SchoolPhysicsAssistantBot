import handlers

from aiogram import executor
from utils.notify_admin import notify_admin
from utils.set_commands import bot_commands

from loader import dp


async def start_bot_info(dp):
    '''function calls other functions to load initial commands and settings for the admin'''
    #send message to admin of bot online
    await notify_admin(dp)
    #load standart command
    await bot_commands(dp)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup = start_bot_info)
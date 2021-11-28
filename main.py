import handlers

from aiogram import executor
from utils.notify_admin import notify_admin
from utils.set_commands import bot_commands

from loader import dp

async def start_bot_info(dp):
    #Пишем в личные сообщенеия админу(-ам) о запуске бота
    await notify_admin(dp)
    #Установка стандартных команд
    await bot_commands(dp)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup = start_bot_info)
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )

storage = MemoryStorage()  # create copy MemoryStorage

bot = Bot(token=config.TOKEN, parse_mode="HTML")  # create copy Bot
dp = Dispatcher(bot, storage=storage)  # create copy Dispatcher

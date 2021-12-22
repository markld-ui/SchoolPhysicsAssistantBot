from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token = config.TOKEN, parse_mode = "HTML") #create copy Bot
storage = MemoryStorage() # create copy MemoryStorage
dp = Dispatcher(bot, storage = storage) #create copy Dispatcher
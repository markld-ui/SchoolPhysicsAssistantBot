import logging

from aiogram import Bot, Dispatcher, types
from handlers.Start.start import router

from data import config

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )

bot = Bot(token=config.TOKEN, parse_mode="HTML")  # create copy Bot
dp = Dispatcher() # create copy Dispatcher
dp.include_router(router)

# SchoolPhysicsAssistantBot

![PyPI](https://img.shields.io/pypi/v/PyPI?color=gree&label=PyPI&style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiogram?color=gree&label=Python&logoColor=blue&style=plastic)

**THIS CODE ISN'T OPEN SOURCE. He was be developed for to protect the project.**

**SchoolPhysicsAssistantBot** - This is an assistant bot for students in grades 7-11 of high school. He will help you quickly pick up the law and the formula for it, if the student has forgotten this information.

___

## ___Usage___
You can generate your bot token for working on it from @BotFather and insert it into your configuration file (in my case, in ".env")

```.env
TOKEN = your token bot
```
After that, use it in your program.

__File: _data/config.py___

The ".env" file is not present in the repository, but you can create it yourself or do it differently.
```python
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN") # get token-bot from .env file
ADMINS = env.list("ADMINS") # get id administrator (programmer) from .env file
```

__File: _loader.py___
```python
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
```

## ___Example echo bot___

After setting up our bot at @BotFather, we will write a simple bot that will repeat our messages after us. This code has been taken from the official documantation of library aiogram

__Exemple file: _echo.py___
```python
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
```
### _Result echo bot_
![](https://i1.wp.com/www.andreafortuna.org/wp-content/uploads/2017/11/Bot2.jpg?ssl=1)

___

## ___Exemple code in project___

__File: _handlers\HelperClient\AllTems\Class11\class11_tems.py___

This file contains data sending, in accordance with the user's request.

```python
from aiogram import types
from aiogram.types import InputMediaPhoto, FSInputFile
from loader import dp
from handlers.HelperClient.ClassTypes.Handbook.class11 import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == '11.1')
async def formuls(message : types.Message):
    '''function for 11.1 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice],resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Электродинамика 11 класс". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media1 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\11class\\electrodinamicap1.jpg'))
    media2 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\11class\\electrodinamicap2.jpg'))
    media3 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\11class\\electrodinamicap3.jpg'))
    media4 = InputMediaPhoto(type = 'photo', media = FSInputFile ('utils\\media\\image\\11class\\electrodinamicap4.jpg'))
    media5 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\11class\\electrodinamicap5.jpg'))
    media = [media1, media2, media3, media4, media5]
    await bot.send_media_group(message.chat.id, media=media)


@dp.message(lambda message: message.text == '11.2')
async def formuls(message : types.Message):
    '''function for 11.2 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Физика высоких энергий". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    photo = FSInputFile('utils\\media\\image\\11class\\physicshughtenergy.jpg')
    await bot.send_photo(chat_id = message.chat.id, photo = photo)


@dp.message(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button], resize_keyboard = True)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )
```

___

## ___The project was made by:___

+ Slinkov Roman. Bot programming. Graduate of the state school 197, Yekaterinburg, Russia. Now student of Tomsk State University of Control Systems and Radioelectronics

+ Kuzmin Alexey Alexandrovich. Curator of the project. Making edits and assistance in project design.

___

## ___In future:___

+ Branch with files in accordance with programm university will be created
+ Optimisation will be improved
+ This bot probably will be deployed on hosting

___

## ___Links___

- [X] Programmer language: [Python](https://www.python.org)
- [X] Documentation aiogram lib: [aiogram](https://docs.aiogram.dev/en/latest/index.html)
- [X] Telegram Bot API: [API](https://core.telegram.org/bots/api)
- [X] Information for bot:
  - Formuls for 7 class: [web-site](https://zakon-oma.ru/formuly-po-fizike-7-klassa.php)
  - Formuls for 8 class: [web-site](https://zakon-oma.ru/formuly-po-fizike-8-klassa.php)
  - Formuls for 9 class: [web-site](https://zakon-oma.ru/formuly-po-fizike-9-klassa.php)
  - Formuls for 10 class: [web-site](https://zakon-oma.ru/formuly-po-fizike-10-klassa.php)
  - Formuls for 11 class: [web-site](https://zakon-oma.ru/formuly-po-fizike-11-klassa.php)
"# testtgbot"

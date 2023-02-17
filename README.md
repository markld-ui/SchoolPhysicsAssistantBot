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
from opcode import hasconst
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN") # get token-bot from .env file
ADMINS = env.list("ADMINS") # get id administrator (programmer) from .env file
HOST =  env.str("HOST")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
```

__File: _loader.py___
```python
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token = config.TOKEN, parse_mode = "HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage = storage)
```

## ___Exemple echo bot___

After setting up our bot at @BotFather, we will write a simple bot that will repeat our messages after us.

__Exemple file: _echo.py___
```python
from aiogram import Bot, Dispatcher, types, executor
from data import config


bot = Bot(token = config.TOKEN, parse_mode = 'HTML')
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
```
### _Result echo bot_
![](https://i1.wp.com/www.andreafortuna.org/wp-content/uploads/2017/11/Bot2.jpg?ssl=1)

___

## ___Exemple code in project___

__File: _handlers\HelperClient\AllTems\Class11\class11_tems.py___

This file contains data sending, in accordance with the user's request.

```python
from aiogram import types
from loader import dp
from handlers.HelperClient.ClassTypes.Handbook.class11 import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot


@dp.message_handler(lambda message: message.text == '11.1')
async def formuls(message : types.Message):
    '''function for 11.1 theme'''
    media = types.MediaGroup()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Электродинамика 11 класс". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media.attach_photo(types.InputFile('utils\\image\\11class\\electrodinamicap1.jpg'))
    media.attach_photo(types.InputFile('utils\\image\\11class\\electrodinamicap2.jpg'))
    media.attach_photo(types.InputFile('utils\\image\\11class\\electrodinamicap3.jpg'))
    media.attach_photo(types.InputFile('utils\\image\\11class\\electrodinamicap4.jpg'))
    media.attach_photo(types.InputFile('utils\\image\\11class\\electrodinamicap5.jpg'))
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_media_group(message.chat.id, media=media)
    

@dp.message_handler(lambda message: message.text == '11.2')
async def formuls(message : types.Message):
    '''function for 11.2 theme'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Физика высоких энергий". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_chat_action(message.from_user.id, types.chat.ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\11class\\physicshughtenergy.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )
```

___

## ___The project was made by:___

+ Slinkov Roman. Bot programming. Learner MAOU SOSH 197, Yekaterinburg, Russia.
+ Kuzmin Alexey Alexandrovich. Curator of the project. Making edits and assistance in project design.

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

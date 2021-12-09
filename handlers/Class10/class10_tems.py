from aiogram import types
from loader import dp
from handlers.ClassTypes.class10 import array_choice
from handlers.ClassTypes.choice_class import class_button
from loader import bot


@dp.message_handler(lambda message: message.text == '10.3')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Электродинамика за 10 класс". Пожалуйста:',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\electrodinamica.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == '10.1')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Выми выбрана тема "Механика". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\mechanicap1.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\mechanicap2.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\mechanicap3.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\mechanicap4.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\mechanicap5.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\mechanicap6.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == '10.2')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Молекулярная физика". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\moleculyarnayap1.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\10class\\moleculyarnayap2.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )
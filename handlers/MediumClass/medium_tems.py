from aiogram import types
from loader import dp
from handlers.ClassTypes.medium_class import array_choice
from handlers.ClassTypes.choice_class import class_button
from loader import bot


@dp.message_handler(lambda message: message.text == 'Тепловые явления')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\8class\\teplovieyavleniyap1.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\8class\\teplovieyavleniyap2.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Электрические явления')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\8class\\electricheskieyavleniyap1.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\8class\\electricheskieyavleniyap2.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Электромагнитные явления')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\8class\\electromagnitnieyavleniya.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Световые явления')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\8class\\svetovieyacleniya.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )
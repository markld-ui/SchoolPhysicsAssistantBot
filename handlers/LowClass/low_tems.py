from aiogram import types
from loader import dp
from handlers.ClassTypes.low_class import array_choice
from handlers.ClassTypes.choice_class import class_button
from loader import bot


@dp.message_handler(lambda message: message.text == 'Взаимодействие тел')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\7class\\vzaimodeistvietel.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Давление твёрдых тел, жидкостей и газов')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\7class\\davlenietvteljidciproch.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Работа, энергия, мощность')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = False)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\7class\\rabotaimoshnostp1.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\7class\\rabotaimoshnostp2.jpg', 'rb'))


'''
@dp.message_handler(lambda message: message.text == 'Давление, сила давления')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\7class\\davlenie.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Давление газов и жидкостей')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\7class\\davleniejidcostiigazov.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Работа, энергия, мощность')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\7class\\rabota.jpg', 'rb'))
'''


@dp.message_handler(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )
from aiogram import types
from loader import dp
from handlers.ClassTypes.hight_class import array_choice
from handlers.ClassTypes.choice_class import class_button
from loader import bot


@dp.message_handler(lambda message: message.text == '9.1')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Законы взаимодействия и движения тел". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp1.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp2.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp3.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp4.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp5.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == '9.2')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Электромагнитное поле". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\electromagnitnoepolep1.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\electromagnitnoepolep2.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\electromagnitnoepolep3.jpg', 'rb'))
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\electromagnitnoepolep4.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == '9.3')
async def formuls(message : types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*array_choice)
    await message.reply(
    'Вами выбрана тема "Строение атома и атомного ядра". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    await bot.send_photo(chat_id = message.chat.id, photo = open('utils\\image\\9class\\stroenieatomyadra.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*class_button)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )
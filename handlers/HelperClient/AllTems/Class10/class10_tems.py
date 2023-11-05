from aiogram import types
from aiogram.types import InputMediaPhoto, FSInputFile
from loader import dp
from handlers.HelperClient.ClassTypes.Handbook.class10 import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == '10.1')
async def formuls(message : types.Message):
    '''function for 10.1 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice],resize_keyboard = True)
    await message.reply(
    'Выми выбрана тема "Механика". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media1 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\10class\\mechanicap1.jpg'))
    media2 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\10class\\mechanicap2.jpg'))
    media3 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\10class\\mechanicap3.jpg'))
    media4 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\10class\\mechanicap4.jpg'))
    media5 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\10class\\mechanicap5.jpg'))
    media6 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\10class\\mechanicap6.jpg'))
    media = [media1,media2,media3,media4,media5,media6]
    await bot.send_media_group(message.chat.id, media=media)


@dp.message(lambda message: message.text == '10.2')
async def formuls(message : types.Message):
    '''function for 10.2 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice],resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Молекулярная физика". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media1 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\10class\\moleculyarnayap1.jpg'))
    media2 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\10class\\moleculyarnayap2.jpg'))
    media = [media1, media2]
    await bot.send_media_group(message.chat.id, media=media)


@dp.message(lambda message: message.text == '10.3')
async def formuls(message : types.Message):
    '''function for 10.2 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice],resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Электродинамика за 10 класс". Пожалуйста:',
    reply = False,
    reply_markup = keyboard)
    photo = FSInputFile('utils\\media\\image\\10class\\electrodinamica.jpg')
    await bot.send_photo(chat_id = message.chat.id, photo = photo)


@dp.message(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button],resize_keyboard = True)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )
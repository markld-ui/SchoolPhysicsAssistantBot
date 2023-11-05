from aiogram import types
from loader import dp
from aiogram.types import InputMediaPhoto, FSInputFile
from handlers.HelperClient.ClassTypes.Handbook.medium_class import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == '8.1')
async def formuls(message : types.Message):
    '''function for 8.1 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Тепловые явления". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media1 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\8class\\teplovieyavleniyap1.jpg'))
    media2 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\8class\\teplovieyavleniyap2.jpg'))
    media = [media1, media2]
    await bot.send_media_group(message.chat.id, media=media)


@dp.message(lambda message: message.text == '8.2')
async def formuls(message : types.Message):
    '''function for 8.2 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Электрические явления". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media1 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\8class\\electricheskieyavleniyap1.jpg'))
    media2 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\8class\\electricheskieyavleniyap2.jpg'))
    media = [media1, media2]
    await bot.send_media_group(message.chat.id, media=media)


@dp.message(lambda message: message.text == '8.3')
async def formuls(message : types.Message):
    '''function for 8.3 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Электромагнитные явления". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    photo = FSInputFile('utils\\media\\image\\8class\\electromagnitnieyavleniya.jpg')
    await bot.send_photo(chat_id = message.chat.id, photo = photo)


@dp.message(lambda message: message.text == '8.4')
async def formuls(message : types.Message):
    '''function for 8.4 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Световые явления". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    photo = FSInputFile('utils\\media\\image\\8class\\svetovieyacleniya.jpg')
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
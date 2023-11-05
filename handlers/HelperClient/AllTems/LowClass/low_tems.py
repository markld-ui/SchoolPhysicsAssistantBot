from aiogram import types
from loader import dp
from aiogram.types import InputMediaPhoto, FSInputFile
from handlers.HelperClient.ClassTypes.Handbook.low_class import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == '7.1')
async def formuls(message : types.Message):
    '''function for 7.1 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Взаимодействие тел". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    photo = FSInputFile('utils\\media\\image\\7class\\vzaimodeistvietel.jpg')
    await bot.send_photo(chat_id = message.chat.id, photo = photo)


@dp.message(lambda message: message.text == '7.2')
async def formuls(message : types.Message):
    '''function for 7.2 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Давление твёрдых тел, жидкостей и газов". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    photo = FSInputFile('utils\\media\\image\\7class\\davlenietvteljidciproch.jpg')
    await bot.send_photo(chat_id = message.chat.id, photo = photo)


@dp.message(lambda message: message.text == '7.3')
async def formuls(message : types.Message):
    '''function for 7.3 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice], resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Работа, энергия, мощность". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media1 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\7class\\rabotaimoshnostp1.jpg'))
    media2 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\7class\\rabotaimoshnostp2.jpg'))
    media = [media1, media2]
    await bot.send_media_group(message.chat.id, media = media)


@dp.message(lambda message: message.text == 'Выход')
async def exit(message: types.Message):
    '''function for exit in choice class'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*class_button], resize_keyboard = True)
    await message.reply(
    'Выберите класс, в котором хотите посмотреть новые формулы:',
    reply = False,
    reply_markup = keyboard
    )
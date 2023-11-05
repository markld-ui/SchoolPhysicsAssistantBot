from aiogram import types
from aiogram.types import InputMediaPhoto, FSInputFile
from loader import dp
from handlers.HelperClient.ClassTypes.Handbook.hight_class import array_choice
from handlers.HelperClient.ClassTypes.choice_class import class_button
from loader import bot
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


@dp.message(lambda message: message.text == '9.1')
async def formuls(message : types.Message):
    '''function for 9.1 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice],resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Законы взаимодействия и движения тел". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media1 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp1.jpg'))
    media2 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp2.jpg'))
    media3 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp3.jpg'))
    media4 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp4.jpg'))
    media5 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\zakonivzaimodeistviyaidvijeniyatelp5.jpg'))
    media = [media1, media2, media3, media4, media5]
    await bot.send_media_group(message.chat.id, media = media)


@dp.message(lambda message: message.text == '9.2')
async def formuls(message : types.Message):
    '''function for 9.2 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice],resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Электромагнитное поле". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    media1 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\electromagnitnoepolep1.jpg'))
    media2 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\electromagnitnoepolep2.jpg'))
    media3 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\electromagnitnoepolep3.jpg'))
    media4 = InputMediaPhoto(type = 'photo', media = FSInputFile('utils\\media\\image\\9class\\electromagnitnoepolep4.jpg'))
    media = [media1, media2, media3, media4]
    await bot.send_media_group(message.chat.id, media = media)

@dp.message(lambda message: message.text == '9.3')
async def formuls(message : types.Message):
    '''function for 9.3 theme'''
    keyboard = ReplyKeyboardMarkup(keyboard=[*array_choice],resize_keyboard = True)
    await message.reply(
    'Вами выбрана тема "Строение атома и атомного ядра". Пожалуйста: ',
    reply = False,
    reply_markup = keyboard)
    photo = FSInputFile('utils\\media\\image\\9class\\stroenieatomyadra.jpg',)
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
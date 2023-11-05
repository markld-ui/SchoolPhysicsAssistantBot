from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Привет!\n'
                        'Я твой персональный бот-помощник по физике.\n'
                        'Начнём?'
        ),
        BotCommand(
            command='help',
            description=
            '''
Мои команды:
    - /help
    - /start

Нажмите на одну из кнопок, чтобы перейти к выбору метода образования
        ''',
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault)
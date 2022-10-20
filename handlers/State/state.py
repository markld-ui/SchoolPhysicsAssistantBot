from aiogram.dispatcher.filters.state import StatesGroup, State


class NewUser(StatesGroup):
    Name = State()
    Class = State()
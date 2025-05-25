from io import BytesIO

from aiogram import types, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from database.constants import *

from bot.bot import Users, bot

router_admin = Router()


async def send_update():
    data = Users.get_data()
    print(data)

    keyboard = make_keyboard_inline(['Принять', 'Отказать'], 2)
    message = data[2] if data[2] != '-' else 'Текст отсутствует'

    text = f"Сообщение номер {data[1]} от {data[5]}:\n\n{message}"
    if data[2] != '-':
        for i in ADMINS:
            await bot.send_message(chat_id=i, text=text, parse_mode='Markdown', reply_markup=keyboard)


def main():
    pass



main()

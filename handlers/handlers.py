from io import BytesIO

from aiogram import types, F, Router, Bot
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from database.constants import *


router = Router()


def main():
    @router.message(F.text, Command('start'))
    async def start(message: types.Message):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        text='ку'

        await message.answer(text=text, reply_markup=make_keyboard(['Помощь', 'О партии'], 2))


main()
from io import BytesIO

from aiogram import types, F, Router, Bot
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from database.constants import *
from bot.bot import Users, bot

router_for_callbacks = Router()


def main():
    @router_for_callbacks.callback_query(F.data.startswith('П'))
    async def callback_accept(callback_query: types.CallbackQuery):
        res = callback_query.data.split('_')
        num = int(res[1])
        data = Users.get_data_from_num(num)

        if not data[4]:
            text = (f'<b>Поздравляем!</b> Ваше сообщение <u>№{data[1]}</u> было принято админом.'
                    f' Ожидайте публикацию сообщения в канале.')


            await bot.send_message(chat_id=data[0], text=text)
            Users.change_process(num)
            await callback_query.answer()

    @router_for_callbacks.callback_query(F.data.startswith('О'))
    async def callback_accept(callback_query: types.CallbackQuery):
        res = callback_query.data.split('_')
        num = int(res[1])
        data = Users.get_data_from_num(num)

        if not data[4]:
            text = f'<b>К сожалению</b>, ваше сообщение <u>№{data[1]}</u> не было принято админом.'

            await bot.send_message(chat_id=data[0], text=text)
            Users.change_process(num)
            await callback_query.answer()


main()

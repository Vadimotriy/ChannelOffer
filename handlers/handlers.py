from io import BytesIO

from aiogram import types, F, Router, Bot
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from database.constants import *

from bot.bot import Users
from handlers.admin import send_update

router = Router()


def main():
    @router.message(F.text, Command('start'))
    async def start(message: types.Message):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        text = (f'Доброго времени суток, товарищь {message.from_user.first_name}!\n\n'
                f'Отправляй свои идеи и предложения сюда, а наши администраторы просмотрят их и решат,'
                f' что попадет на канал.')
        await message.answer(text=text, reply_markup=make_keyboard(['Помощь', 'О партии'], 2))

    @router.message(F.text == 'Помощь')
    async def help_user(message: types.Message):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        text = (
            'Здравствуйте! Перед тем как вы расскажите нам о своей идее, мы расскажем, что точно не будет одобрено.\n\n'
            'Что точно <u>не будет</u> принято:\n'
            '\t1. Всё что запрещено законом (наркотики, экстремизм, расизм и тд.);\n'
            '\t2. Материал сексуального характера;\n'
            '\t3. Реклама чего-либо;\n'
            '\t4. Сообщения, содержащие нецензурную лексику.\n'
        )
        await message.answer(text=text)

    @router.message(F.text == 'О партии')
    async def help_user(message: types.Message):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        text = (
            'Наша партия создана исключительно в развлекательных целях, ставя перед собой  '
            'объединения людей со схожими взглядами и увлечениями, для хорошего времяпровождения.'
        )
        await message.answer(text=text)

    @router.message()
    async def message(message: types.Message, bot: Bot):

        try:
            image = BytesIO()
            await bot.download(message.photo[-1], destination=image)
            image = image.getvalue()
        except TypeError:
            image = '-'

        try:
            text = message.text
        except TypeError:
            text = '-'

        num = Users.get_data(num='Num')
        Users.add_message(message.from_user.id, num + 1, text, message.from_user.full_name, image)

        text = f'Вашему сообщению присвоен номер {num + 1}, ожидайте ответа от администраторов.'
        await message.reply(text=text)
        await send_update()



main()

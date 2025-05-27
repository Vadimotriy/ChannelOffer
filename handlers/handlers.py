from aiogram import types, F, Router, Bot
from aiogram.filters import Command
from database.functions import *

from bot.bot import Users, ADMINS
from handlers.admin import send_update
from database.constants import *

router = Router()


def main():
    # /start
    @router.message(F.text, Command('start'))
    async def start(message: types.Message):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        text = start_text(message.from_user.first_name)
        await message.answer(text=text, reply_markup=make_keyboard(['Помощь', 'О канале'], 2))

    # помощь пользователю
    @router.message(F.text == 'Помощь')
    async def help_user(message: types.Message):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        text = HELP_TEXT
        await message.answer(text=text)

    # информация о канале для пользователя
    @router.message(F.text == 'О канале')
    async def help_user(message: types.Message):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        text = ABOUT_TEXT
        await message.answer(text=text)

    # отправка текстовых сообщений на рассмотрение админам
    @router.message(F.text)
    async def message(message: types.Message, bot: Bot):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        image = '-'
        text = message.text

        num = Users.get_data(num='Num')
        Users.add_message(message.from_user.id, num + 1, text, message.from_user.first_name, image)

        text = f'Вашему сообщению присвоен №{num + 1}, ожидайте ответа от администраторов.'
        await message.reply(text=text)
        await send_update()

    # отправка фотографий на рассмотрение админам
    @router.message(F.photo)
    async def message(message: types.Message, bot: Bot):
        if message.from_user.id not in ADMINS:
            await message.reply('Вы админ!')
            return

        photo = message.photo[-1]
        file = await bot.get_file(photo.file_id)
        file_path = file.file_path
        photo_bytes = await bot.download_file(file_path)

        image = base64.b64encode(photo_bytes.read()).decode('utf-8')
        text = message.caption
        if not text:
            text = '-'

        num = Users.get_data(num='Num')
        Users.add_message(message.from_user.id, num + 1, text, message.from_user.first_name, image)

        text = f'Вашему сообщению присвоен №{num + 1}, ожидайте ответа от администраторов.'
        await message.reply(text=text)
        await send_update()


main()

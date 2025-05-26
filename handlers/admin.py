import base64
from io import BytesIO
from PIL import Image

from aiogram import F, Router
from aiogram.types import BufferedInputFile
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from database.constants import *

from bot.bot import Users, bot, ADMINS

router_admin = Router()


def restore_from_base64_to_bytesio(base64_string):
    image_data = base64.b64decode(base64_string)

    image = Image.open(BytesIO(image_data))
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)

    return img_byte_arr.getvalue()


async def send_update():
    data = Users.get_data()

    message = data[2] if data[2] != '-' else 'Текст отсутствует'
    text = f"Сообщение номер {data[1]} от {data[5]}:\n\n{message}"

    if data[2] != '-' and data[3] == '-':
        for i in ADMINS:
            keyboard = make_keyboard_inline(['Принять', 'Отказать'], 2, data[1], i)
            await bot.send_message(chat_id=i, text=text, parse_mode='Markdown', reply_markup=keyboard)
    else:
        for i in ADMINS:
            image = restore_from_base64_to_bytesio(data[3])
            photo = BufferedInputFile(image, filename='restored_image.jpeg')

            keyboard = make_keyboard_inline(['Принять', 'Отказать'], 2, data[1], i)
            await bot.send_photo(chat_id=i, caption=text, parse_mode='Markdown', reply_markup=keyboard, photo=photo)


def main():
    pass



main()

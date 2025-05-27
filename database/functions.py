import base64
from io import BytesIO
from PIL import Image

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import BufferedInputFile, CallbackQuery, InlineKeyboardButton, KeyboardButton


# клавиатура для пользователя
def make_keyboard(buttons, adjust):
    builder = ReplyKeyboardBuilder()
    for i in buttons:
        builder.add(KeyboardButton(text=i))
    builder.adjust(adjust)

    return builder.as_markup()


# создание инлайн клавиатуры для админов
def make_keyboard_inline(buttons, adjust, num, admin):
    builder = InlineKeyboardBuilder()
    for i in buttons:
        builder.add(InlineKeyboardButton(text=i, callback_data=f'{i[0]}_{num}_{admin}'))
    builder.adjust(adjust)

    return builder.as_markup()


# декодировка изображений, для aiogram
def decode_image(base64_string):
    image_data = base64.b64decode(base64_string)

    image = Image.open(BytesIO(image_data))
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    image = img_byte_arr.getvalue()
    photo = BufferedInputFile(image, filename='restored_image.jpeg')

    return photo

# изменение сообщений
async def update(callback: CallbackQuery, update: str, image):
    if image == '-':  # когда нет фотографий
        await callback.message.edit_text(update)
    else:  # когда есть
        await callback.message.edit_caption(caption=update)


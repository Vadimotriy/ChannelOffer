from database.constants import *
from bot.bot import Users, bot, ADMINS


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
            photo = decode_image(data[3])
            keyboard = make_keyboard_inline(['Принять', 'Отказать'], 2, data[1], i)

            await bot.send_photo(chat_id=i, caption=text, parse_mode=None, reply_markup=keyboard, photo=photo)


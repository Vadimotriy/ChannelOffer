from database.functions import *
from bot.bot import Users, bot, ADMINS


# отправка сообщений админам
async def send_update():
    data = Users.get_data()

    message = data[2] if data[2] != '-' else 'Текст отсутствует'
    text = f"Сообщение номер {data[1]} от {data[5]}:\n\n{message}"
    keyboard = make_keyboard_inline(['Принять', 'Отказать'], 2, data[1], i)

    if data[2] != '-' and data[3] == '-':  # без фотграфии
        for i in ADMINS:
            try:
                await bot.send_message(chat_id=i, text=text, parse_mode='Markdown', reply_markup=keyboard)
            except Exception:
                pass

    else:  # с фотографией
        for i in ADMINS:
            try:
                photo = decode_image(data[3])
                await bot.send_photo(chat_id=i, caption=text, parse_mode=None, reply_markup=keyboard, photo=photo)
            except Exception:
                pass

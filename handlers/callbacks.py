from aiogram import F, Router
from database.functions import *
from bot.bot import Users, bot, CHANNEL_ID

router_for_callbacks = Router()


def main():
    # отправка сообщений в канал
    async def send_to_channel(data):
        text, image = data[2], data[3]
        if image == '-':
            text = text + '\n\n*Прислано подписчиком*'
            await bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode='Markdown')

        else:
            photo = decode_image(image)
            if text == '-':
                text = 'Прислано подписчиком'
            else:
                text = text + '\n\nПрислано подписчиком'

            await bot.send_photo(chat_id=CHANNEL_ID, caption=text, parse_mode=None, photo=photo)

    # принятие сообщения
    @router_for_callbacks.callback_query(F.data.startswith('П'))
    async def callback_accept(callback_query: CallbackQuery):
        res = callback_query.data.split('_')
        num = int(res[1])
        data = Users.get_data_from_num(num)

        if not data[4]:  # успешное принятие
            text = (f'<b>Поздравляем!</b> Ваше сообщение <u>№{data[1]}</u> было принято админом.'
                    f' Ожидайте публикацию сообщения в канале.')

            await bot.send_message(chat_id=data[0], text=text)
            Users.change_process(num)
            await update(callback_query, '🔄 Идет отправка сообщения на канал!', data[3])

            await send_to_channel(data)
            await update(callback_query, '✅ Сообщение отправлено на канал!', data[3])
            await callback_query.answer()
        else:  # кто-то из админов уже принял/отклонил
            text = 'отклонил' if data[4] == 2 else 'принял'
            await update(callback_query, f'‼️Кто-то уже {text} сообщение‼️', data[3])
            await callback_query.answer()

    # отклонение предложения
    @router_for_callbacks.callback_query(F.data.startswith('О'))
    async def callback_accept(callback_query: CallbackQuery):
        res = callback_query.data.split('_')
        num = int(res[1])
        data = Users.get_data_from_num(num)

        if not data[4]:  # успешное отклонение
            text = f'<b>К сожалению</b>, ваше сообщение <u>№{data[1]}</u> не было принято админом.'

            await bot.send_message(chat_id=data[0], text=text)
            Users.change_process(num, 2)
            await update(callback_query, '❌ Сообщение отклонено!', data[3])
            await callback_query.answer()
        else:  # кто-то из админов уже принял/отклонил
            text = 'отклонил' if data[4] == 2 else 'принял'
            await update(callback_query, f'‼️Кто-то уже {text} сообщение‼️', data[3])
            await callback_query.answer()


main()

from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def make_keyboard(buttons, adjust):
    builder = ReplyKeyboardBuilder()
    for i in buttons:
        builder.add(types.KeyboardButton(text=i))
    builder.adjust(adjust)

    return builder.as_markup()


def make_keyboard_inline(buttons, adjust, num, admin):
    builder = InlineKeyboardBuilder()
    for i in buttons:
        builder.add(types.InlineKeyboardButton(text=i, callback_data=f'{i[0]}_{num}_{admin}'))
    builder.adjust(adjust)

    return builder.as_markup()




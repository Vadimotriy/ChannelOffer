from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def make_keyboard(buttons, adjust):
    builder = ReplyKeyboardBuilder()
    for i in buttons:
        builder.add(types.KeyboardButton(text=i))
    builder.adjust(adjust)

    return builder.as_markup()


def make_keyboard_inline(buttons, adjust):
    builder = InlineKeyboardBuilder()
    for i in buttons:
        builder.add(types.InlineKeyboardButton(text=i))
    builder.adjust(adjust)

    return builder.as_markup()


ADMINS = [5240953558, 1602858870]

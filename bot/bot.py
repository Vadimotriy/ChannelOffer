import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from database.users import MyDict


logging.basicConfig(level=logging.INFO)

load_dotenv('data/.env')
API_TOKEN = os.getenv("API_TELEGRAM")
ADMINS = [os.getenv("ADMINS")]

Users = MyDict()
Users.add_message(1, 1, 'das', 'asd')

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

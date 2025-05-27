import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from database.users import MyDict

# логирование
logging.basicConfig(level=logging.INFO)

# достаем данные из .env файла
load_dotenv('data/.env')
API_TOKEN = os.getenv("API_TELEGRAM")
ADMINS = os.getenv("ADMINS").split('_')
CHANNEL_ID = os.getenv("CHANNEL_ID")

Users = MyDict()
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

import requests
from config import token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привет, этот бот хочет унизить тебя, оскорбляй его в ответ если не хочешь остаться терпилой")

@dp.message_handler()
async def get_ban(message: types.Message):
    req = requests.get('https://evilinsult.com/generate_insult.php?lang=ru&type=json')
    ban = req.json()['insult']
    await message.answer(ban)

if __name__ == '__main__':
    executor.start_polling(dp)
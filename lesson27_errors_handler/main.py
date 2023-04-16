import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BotBlocked

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await asyncio.sleep(10)
    await message.answer('some text')


@dp.errors_handler(exception=BotBlocked)
async def error_handler(update: types.Update, exception: BotBlocked) -> bool:
    print("can't send message")
    return True


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

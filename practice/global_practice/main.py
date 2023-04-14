from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Start bot")

if __name__ == "__main__":
    executor.start_polling(skip_updates=True, on_startup=on_startup)

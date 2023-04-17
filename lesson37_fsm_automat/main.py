from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from config import TOKEN

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot,
                storage=storage)


class ProfileStatesGroup(StatesGroup):
    photo = State()
    name = State()
    age = State()
    descr = State()


def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/create'))
    return kb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Welcome. Create profile',
                         reply_markup=get_keyboard())


@dp.message_handler(commands=['create'])
async def create_start(message: types.Message) -> None:
    await message.reply('Start create your profile: send your photo')
    await ProfileStatesGroup.photo.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

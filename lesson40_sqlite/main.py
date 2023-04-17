from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from sqlite import edit_profile, create_profile, db_start

from config import TOKEN

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot,
                storage=storage)


async def on_startup(_):
    await db_start()


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
    await create_profile(user_id=message.from_user.id)


@dp.message_handler(commands=['create'])
async def create_start(message: types.Message) -> None:
    await message.reply('Start create your profile: send your photo')
    await ProfileStatesGroup.photo.set()


@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message) -> None:
    await message.reply('This is not photo',
                        reply_markup=get_keyboard())


@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.reply('Send your name')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.name)
async def set_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply('Send your age')
    await ProfileStatesGroup.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ProfileStatesGroup.age)
async def check_age(message: types.Message) -> None:
    await message.reply('Enter your age like number',
                        reply_markup=get_keyboard())


@dp.message_handler(state=ProfileStatesGroup.age)
async def set_age(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text

    await message.reply('Send about you')
    await ProfileStatesGroup.next()


@dp.message_handler(state=ProfileStatesGroup.descr)
async def set_descr(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['descr'] = message.text
        print(data)
        await bot.send_photo(message.from_user.id,
                             photo=data['photo'],
                             caption=f"Saved profile - {data['name']}, {data['age']}\n{data['descr']}")
    await edit_profile(state, user_id=message.from_user.id)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

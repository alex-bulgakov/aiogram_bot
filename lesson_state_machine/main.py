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


class ClientStatesGroup(StatesGroup):
    photo = State()
    desc = State()


def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Go work'))
    return kb


def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('heeelllooo',
                         reply_markup=get_keyboard())


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state:
        await message.reply('Canceled',
                            reply_markup=get_keyboard())
        await state.finish()


@dp.message_handler(Text(equals='Go work', ignore_case=True), state=None)
async def go_work(message: types.Message) -> None:
    await ClientStatesGroup.photo.set()
    await message.answer('First send photo',
                         reply_markup=get_cancel())


@dp.message_handler(lambda message: not message.photo, state=ClientStatesGroup.photo)
async def check_photo(message: types.Message):
    return await message.reply("It's not a photo")  # why return?


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await ClientStatesGroup.next()
    await message.reply('Send description of photo')


@dp.message_handler(state=ClientStatesGroup.desc)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text

    await message.reply('Photo saved')

    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=data['desc'])

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

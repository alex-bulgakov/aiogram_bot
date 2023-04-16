import random
from time import sleep

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from practice.global_practice.keyboards import kb, kb2, ikb

bot = Bot(TOKEN)
dp = Dispatcher(bot)
message_id = ''

TEXT_HELP = """
<b>/start</b> - start bot
<b>/help</b> - help bot
<b>/description</b> - about bot
<b>/photomenu</b> - menu - get random photo
<b>/getphoto</b> - get random photo
<b>/getemoji</b> - get emoji
<b>/getsticker</b> - get sticker
<b>/getrandomlocation</b> - get random location
"""

urls = [
    ["https://avatars.mds.yandex.net/i?id=5f71d182084704966698ccefd3769d0b50b08bcb-8497046-images-thumbs&n=13&exp=1",
     "photo 1"],
    ["https://avatars.mds.yandex.net/i?id=3255c46bc7ecf108753e1da21cc7282afb9c5baf-4615702-images-thumbs&n=13&exp=1",
     "photo 2"],
    ["https://avatars.mds.yandex.net/i?id=f998b4559f481e3ba35d71bcda59cc66f86c79b2-7629177-images-thumbs&n=13&exp=1",
     "photo 3"],
    ["https://avatars.mds.yandex.net/i?id=ce669bdfab22bed1e4eab239e8240444ee0b8a9d-4579756-images-thumbs&n=13&exp=1",
     "photo 4"],
    ["https://avatars.mds.yandex.net/i?id=013d23aa3415131e4708c155734ee4965c432dba-8223678-images-thumbs&n=13&exp=1",
     "photo 5"]
]

random_photo = random.choice(urls)


async def on_startup(_):
    print("Start bot")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Start bot',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=TEXT_HELP,
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='This is global practice bot')
    await message.delete()


@dp.message_handler(commands=['getphoto'])
async def getphoto_command(message: types.Message):
    await send_random_photo(message.from_user.id)
    await message.delete()


@dp.message_handler(commands=['getemoji'])
async def getemoji_command(message: types.Message):
    await message.answer('😁')
    await message.delete()


@dp.message_handler(commands=['getsticker'])
async def getsticker_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAICTWQ4WFufThVbCxIjigEr3xcfMLRoAAI9DAAC70wRSn94XJTFnf7uLwQ')
    await message.delete()


@dp.message_handler(commands=['getrandomlocation'])
async def getrandomlocation_command(message: types.Message):
    location = await get_random_location()
    await bot.send_location(message.from_user.id,
                            latitude=location['latitude'],
                            longitude=location['longitude'])
    await message.delete()


@dp.message_handler(commands=['photomenu'])
async def photo_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Go to menu - photo',
                           reply_markup=kb2)
    await message.delete()


@dp.message_handler(commands=['mainmenu'])
async def mainmenu_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Go to main menu',
                           reply_markup=kb)
    await message.delete()


async def send_random_photo(id):
    get_random_photo_url()
    await bot.send_photo(chat_id=id,
                   caption=random_photo[1],
                   photo=random_photo[0],
                   reply_markup=ikb)


async def get_random_photo_url():
    global random_photo
    random_photo = random.choice(list(filter(lambda x: x != random_photo, urls)))

async def get_random_location():
    result = {'latitude': random.randint(-90, 90), 'longitude': random.randint(-180, 180)}
    return result


# @dp.callback_query_handler()
# async def sendphoto_callback(callback: types.CallbackQuery):
#     await send_random_photo(callback.message.message_id)
#     callback.message.delete()

@dp.callback_query_handler()
async def photo_callback(callback: types.CallbackQuery):
    global message_id
    if callback.data == "Like":
        if message_id == callback.message.message_id:
            await callback.answer(text="You already push like or dislike")
        else:
            await callback.answer(text="You like it")
    elif callback.data == "Dislike":
        if message_id == callback.message.message_id:
            await callback.answer(text="You already push like or dislike")
        else:
            await callback.answer(text="You dislike it")
    elif callback.data == "Next":
        global random_photo
        await get_random_photo_url()
        await callback.message.edit_media(types.InputMedia(
            media=random_photo[0],
            type='photo',
            caption=random_photo[1]
        ), reply_markup=ikb)
    message_id = callback.message.message_id

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
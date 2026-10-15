import logging

from aiogram import Bot, Dispatcher, executor, types
from search_wiki import get_wiki_page

API_TOKEN = '5928816783:AAFZfSptFPbk03dVDheMbHPe866YlM39qHA'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("How can I help you", reply_markup=menu)


menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
   types.KeyboardButton("WIth Admin")
)

@dp.message_handler()
async def echo(message: types.Message):

    text = message.text
    if text == "WIth Admin":KL
        await message.answer("https://t.me/POSSSIBLESTUDYANDREVISE")
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
import aiogram.utils.markdown as fmt
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def bot_start_command(message: types.Message):
    await message.reply("Привет, назови свое имя!)")


@dp.message_handler(commands=['help'])
async def bot_help_command(message: types.Message):
    await message.reply("Этот бот будет отвечать на твои сообщения.")


@dp.message_handler()
async def greeting_command(message: types.Message):
    await message.answer(fmt.text("Приятно познакомиться: ", fmt.hbold(message.text)), parse_mode=types.ParseMode.HTML)


@dp.message_handler()
async def download_doc(message: types.Message):
    await message.document.download()


@dp.message_handler(content_types=[types.ContentType.STICKER])
async def random_sticker(message: types.Message):
    await message.reply_sticker(message.sticker.file_id)


if __name__ == '__main__':
    executor.start_polling(dp)

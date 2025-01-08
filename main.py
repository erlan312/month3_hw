from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import logging
import os

token = config('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

Admins = [6329594181]

async def on_startup(_):
    for admin in Admins:
            await bot.send_message(chat_id=admin, text='Бот включен!')


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Привет..., {message.from_user.first_name}!\n'
                                    f'Твой Telegram ID: {message.from_user.id}')



@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')

    photo = open(photo_path, 'rb')

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption='Это мем')

@dp.message_handler()
async def echo_or_square_handler(message: types.Message):
    try:

        if message.text.isdigit():
            number = int(message.text)
            squared = number ** 2
            await message.answer(f"Квадрат числа {number} равен {squared}")
        else:

            await message.answer(message.text)
    except Exception as e:
        logging.error(f"Ошибка в обработчике сообщений: {e}")

@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
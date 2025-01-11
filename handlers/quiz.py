# quiz.py
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='button1')
    keyboard.add(button)
    question = 'RM or Barcelona'
    answer = ['RM', 'Barcelona', 'Оба']
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Жаль...',
        open_period=60,
        reply_markup=keyboard
    )

async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('следующее', callback_data='button2')
    keyboard.add(button)
    question = 'DOTA2 or CS.GO'
    answer = ['dota2', 'CS.GO']

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Иди домашку делай дотер',
        open_period=60,
        reply_markup=keyboard
    )


async def quiz_3(call: types.CallbackQuery):

    photo_path = ("media","img_1.png")

    await bot.send_photo(chat_id=call.message.chat.id, photo=open(photo_path, "rb"))

    # Вопрос и ответы для опроса
    question = 'Деньги или любовь'
    answer = ['Деньги', 'Любовь', 'IT']

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation='попался',
        open_period=60
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button1')
    dp.register_callback_query_handler(quiz_3, text='button2')
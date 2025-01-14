from aiogram import types, Dispatcher
from random import sample
from config import bot


dice_options = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def game_dice(message: types.Message):
    selected_dices = sample(dice_options, 3)
    selected_dice = sample(selected_dices, 1)[0]


    bot_message = await bot.send_dice(chat_id=message.chat.id, emoji=selected_dice)
    bot_score = bot_message.dice.value

    user_message = await bot.send_dice(chat_id=message.chat.id, emoji=selected_dice)
    user_score = user_message.dice.value


    if bot_score > user_score:
        await message.answer("Бот выиграл! 🤖")
    elif bot_score < user_score:
        await message.answer("Вы выиграли! 🎉")
    else:
        await message.answer("Ничья! 😎")

def register_game(dp: Dispatcher):
    dp.register_message_handler(game_dice, commands=['game'])

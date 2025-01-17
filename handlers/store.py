from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Store(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    photo = State()


async def start_fsm(message: types.Message):
    await message.answer('Введите название продукта:')
    await Store.name.set()


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton(text='L')
    b2 = KeyboardButton(text='XL')
    b3 = KeyboardButton(text='XXL')
    kb.add(b1, b2, b3)
    await message.answer('Выберите размер продукта:', reply_markup=kb)
    await Store.next()


async def process_size(message: types.Message, state: FSMContext):
    if message.text in ('L', 'XL', 'XXL'):
        async with state.proxy() as data:
            data['size'] = message.text
        await message.answer('Укажите категорию продукта:', reply_markup=ReplyKeyboardRemove())
        await Store.next()
    else:
        await message.answer('Пожалуйста, выберите размер, используя кнопки!')


async def process_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer('Укажите цену продукта:')
    await Store.next()


async def process_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await message.answer('Отправьте фотографию продукта:')
    await Store.next()


async def process_photo(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.answer('Пожалуйста, отправьте фото!')
        return

    photo = message.photo[-1].file_id
    async with state.proxy() as data:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=(
                f"Название: {data['name']}\n"
                f"Размер: {data['size']}\n"
                f"Категория: {data['category']}\n"
                f"Цена: {data['price']}"
            )
        )
    await state.finish()


def register_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=['store'])
    dp.register_message_handler(process_name, state=Store.name)
    dp.register_message_handler(process_size, state=Store.size)
    dp.register_message_handler(process_category, state=Store.category)
    dp.register_message_handler(process_price, state=Store.price)
    dp.register_message_handler(process_photo, state=Store.photo, content_types=['photo'])

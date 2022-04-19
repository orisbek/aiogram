from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Chooose one", reply_markup=menu)

@dp.message_handler(Text(equals=["2E", "4E", "3I"]))
async def get_food(messege:Message):
    await messege.answer(f"Chooosen {messege.text}. Thanks",
                         reply_markup=ReplyKeyboardRemove())
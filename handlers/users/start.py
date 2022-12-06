import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inlineKeyboard import Settings
from keyboards.default.settings import setting
from keyboards.default.Keyboard import menu
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
        
    
    
    
    
    # await message.answer(f"Assalomu aleykum {message.from_user.full_name} Tarjimon botimizga xush kelibsiz tillarni sozlash uchun sozlamar tugmasini bosing!", reply_markup=Settings)
    await message.answer(f"Assalomu aleykum {message.from_user.full_name} Tarjimon botimizga xush kelibsiz tillarni sozlash uchun  sozlamardan tilni sozlang!!" , reply_markup=setting)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
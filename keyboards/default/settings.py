from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
setting=ReplyKeyboardMarkup(
  keyboard = [
        [
            KeyboardButton(text="Tilni sozlash"),
            KeyboardButton(text="Valyuta"),            
         ],
    ],
    resize_keyboard=True
  
)
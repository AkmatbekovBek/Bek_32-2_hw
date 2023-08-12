from config import bot
from aiogram import types, Dispatcher
from database import sql_commands
from const import START_MENU_TEXT
from keyboards.start_kb import admin_select_users_keyboard, start_keyboard



async def start_button(message: types.Message):
    sql_commands.Database().sql_insert_user_cmd(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name)

    print(message)
    with open("E:\pythonProject\Bek_32-2_hw1\helloPhoto.png", "rb") as photo:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=START_MENU_TEXT.format(
                user=message.from_user.username
            ),
            parse_mode=types.ParseMode.MARKDOWN
        )



def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
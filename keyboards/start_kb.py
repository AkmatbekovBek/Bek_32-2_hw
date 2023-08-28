from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
                          KeyboardButton, ReplyKeyboardMarkup





async def admin_select_users_keyboard():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Список Пользователей",
        callback_data="admin_user_list"
    )
    markup.row(
        button_call_1,
    )
    return markup


async def new_start_keyboard():
    markup = InlineKeyboardMarkup()
    random_profiles_button: InlineKeyboardButton = InlineKeyboardButton(
        "Просмотр анкет 🎉",
        callback_data="random_profiles"
    )
    my_profile_button = InlineKeyboardButton(
        "Мой Профиль",
        callback_data="my_profile"
    )
    referral_button = InlineKeyboardButton(
        "Реферальная программа",
        callback_data="reference_menu"
    )
    parser_button = InlineKeyboardButton(
        "Фильмы 🎥",
        callback_data="films_parsing"
    )
    markup.add(
        random_profiles_button
    ).add(
        my_profile_button
    ).add(
        referral_button
    ).add(
        parser_button
    )
    return markup

async def like_dislike_keyboard(telegram_id):
    markup = InlineKeyboardMarkup(row_width=2)
    like_button = InlineKeyboardButton(
        "👍🏻",
        callback_data=f"like_button_{telegram_id}"
    )
    dislike_button = InlineKeyboardButton(
        "👎🏻",
        callback_data="random_profiles"
    )
    markup.row(
        like_button,
        dislike_button
    )
    return markup



async def my_profile_detail_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    update_button = InlineKeyboardButton(
        "Изменить Анкету 💡",
        callback_data="signup"
    )
    delete_button = InlineKeyboardButton(
        "Удаление Анкеты ❌",
        callback_data="delete_profile"
    )
    markup.row(
        update_button,
        delete_button
    )
    return markup


async def if_not_profile_keyboard():
    markup = InlineKeyboardMarkup()
    signup_button = InlineKeyboardButton(
        "Регистрация ✔",
        callback_data="signup"
    )
    markup.row(
        signup_button
    )
    return markup


async def save_films_keyboard(films_id):
    markup = InlineKeyboardMarkup()
    save_button = InlineKeyboardButton(
        "Сохранить 💾",
        callback_data=f"save_films_{films_id}"
    )
    markup.add(
        save_button,
    )
    return markup


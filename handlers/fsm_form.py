from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes


from config import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.sql_commands import Database
from keyboards.fsm_keyboards import select_my_profile_keyboard


class Form_States(StatesGroup):
    nickname = State()
    age = State()
    PlaceOfBirth = State()
    biography = State()
    photo = State()

async def fsm_start(message: types.Message):
    await message.reply('Отправьте свой никнейм:')
    await Form_States.nickname.set()

async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text


    await Form_States.next()
    await message.reply('Отправьте свой возраст (используя числа):')


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        if type(int(message.text)) != int:
            await message.reply('              🔴Ошибка🔴'
                                'Отправьте свой возраст (ИСПОЛЬЗУЯ ЧИСЛА)'
                                '      Запустите регистрацию заново')
            await state.finish()
        else:
            async with state.proxy() as data:
                data['age'] = message.text
            await Form_States.next()
            await message.reply('Отправьте свое место рождения:')
    except ValueError as e:
        await state.finish()
        print(f'FSMAGE: {e}')
        await message.reply('              🔴Ошибка🔴'
                                'Отправьте свой возраст (ИСПОЛЬЗУЯ ЧИСЛА)'
                                '      Запустите регистрацию заново')

async def load_PlaceOfBirth(message: types.Message,
                    state: FSMContext):
    async with state.proxy() as data:
        data['PlaceOfBirth'] = message.text

    await Form_States.next()
    await message.reply("Отправьте свою биографию:")


async def load_biography(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text

    await Form_States.next()
    await message.reply("Отправьте свою фотографию: ")


async def load_photo(message: types.Message,
                     state: FSMContext):
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir="E:\pythonProject\Bek_32-2_hw\media"
    )
    async with state.proxy() as data:

        form_existed = Database().sql_select_user_form_by_telegram_id_command(
            message.from_user.id)
        if form_existed:
            Database().sql_update_user_form_command(
                nickname=data['nickname'],
                age=data['age'],
                PlaceOfBirth=data['PlaceOfBirth'],
                biography=data['biography'],
                photo=path.name,
                telegram_id=message.from_user.id,
            )
            await message.reply("Вы успешно обновили свою анкету\n"
                                "Можете просмотреть свою анкету нажав на кнопку мой профиль",
                                reply_markup=await select_my_profile_keyboard())
        else:
            Database().sql_insert_user_form_command(
                telegram_id=message.from_user.id,
                nickname=data['nickname'],
                age=data['age'],
                PlaceOfBirth=data['PlaceOfBirth'],
                biography=data['biography'],
                photo=path.name,
            )
            await message.reply("Вы успешно зарегистрировали свою анкету\n"
                                "Можете просмотреть свою анкету нажав на кнопку мой профиль",
                                reply_markup=await select_my_profile_keyboard())
    await state.finish()



def register_fsm_form_handlers(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=["signup"])
    dp.register_message_handler(load_nickname,
                                state=Form_States.nickname,
                                content_types=['text'])
    dp.register_message_handler(load_age,
                                state=Form_States.age,
                                content_types=['text'])
    dp.register_message_handler(load_PlaceOfBirth,
                                state=Form_States.PlaceOfBirth,
                                content_types=['text'])
    dp.register_message_handler(load_biography,
                                state=Form_States.biography,
                                content_types=['text'])
    dp.register_message_handler(load_photo,
                                state=Form_States.photo,
                                content_types=ContentTypes.PHOTO)















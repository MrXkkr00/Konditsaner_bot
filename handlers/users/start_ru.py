from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from handlers.users.buyurtma_berish_ru import Sentloco_ru
from handlers.users.tavar_ru import Buyurtma_ru
from keyboards.default.bosh_menu_ru import bosh_menu_ru, mahsulotlar_ru
from keyboards.default.contact_button import  contact_keyboard_ru
from loader import dp


class RegState_ru(StatesGroup):
    name = State()
    number = State()


# class Buyurtma(StatesGroup):
#     tavar = State()
#     middor = State()

# class Sentloco(StatesGroup):
#     loco = State()


@dp.message_handler(text="🏠Меню")
async def bot_staqwequt(message: types.Message):
    await message.answer(f"Выберите нужный раздел", reply_markup=bosh_menu_ru)


#
#
@dp.message_handler(text="🏠Меню", state=[RegState_ru.name, RegState_ru.number])
async def botewqeart_ru(message: types.Message, state:FSMContext):
    await message.answer(f"Выберите нужный раздел", reply_markup=bosh_menu_ru)
    await state.finish()


#
#



#
#
@dp.message_handler(text="🏠Меню", state=[Sentloco_ru.loco])
async def weewqert(message: types.Message, state: FSMContext):
    await message.answer(f"Выберите нужный раздел", reply_markup=bosh_menu_ru)
    await state.finish()

#
#
@dp.message_handler(text="/start", state=[Sentloco_ru.loco])
async def bot__23213art(message: types.Message, state:FSMContext):
    await message.answer(f"Выберите нужный раздел", reply_markup=bosh_menu_ru)
    await state.finish()



#
# @dp.message_handler(text="/start")
# async def bot__rusa53tarta(message: types.Message):
#     await message.answer(f"Assalomu Alaykum!", reply_markup=til)
#
#
# @dp.message_handler(text="/start", state=[RegState_ru.number, RegState_ru.name])
# async def bot_s_ruatarta(message: types.Message):
#     await message.answer(f"Assalomu Alaykum!", reply_markup=til)


@dp.message_handler(text="🇷🇺 Русский")
async def bot_n_ruqwewqame(message: types.Message):
    user_id = message.from_user.id
    f = open("./data/reg/hammasi.txt", "r")
    text = f.read()
    if not str(user_id) in text:
        await message.answer(f"Для регистрации\n"
                              f"Введите ваше имя и фамилию.", reply_markup=ReplyKeyboardRemove())
        await RegState_ru.name.set()
    else:
        await message.answer(f"Выберите нужный раздел", reply_markup=bosh_menu_ru)



@dp.message_handler(state=RegState_ru.name)
async def nqewqwa_rume(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer(f"Отправьте ваш номер", reply_markup=contact_keyboard_ru)
    await RegState_ru.number.set()


@dp.message_handler(lambda message: message.text[:3] in "+998" and len(message.text) == 13, state=RegState_ru.number)
async def con21eqwe31t_ruact(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    number = message.contact.phone_number
    user_id = message.from_user.id

    h = open("./data/reg/hammasi.txt", "a")
    h.write(f"{user_id} {number} {name}\n")
    h.close()

    await message.answer(f"Выберите нужный раздел", reply_markup=bosh_menu_ru)
    await state.finish()


@dp.message_handler(content_types="contact", state=RegState_ru.number)
async def conta_ru1qweq23ct(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    number = message.contact.phone_number
    user_id = message.from_user.id

    h = open("./data/reg/hammasi.txt", "a")
    h.write(f"\n{user_id} {number} {name}")
    h.close()

    await message.answer(f"Выберите нужный раздел", reply_markup=bosh_menu_ru)
    await state.finish()


@dp.message_handler(text="📝 Продукты")
async def na_rumqeqe(message: types.Message):
    await message.answer(f"Выберите категорию", reply_markup=mahsulotlar_ru)

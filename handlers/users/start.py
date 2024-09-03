from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users.buytma_berish import Sentloco
from handlers.users.tavar import Buyurtma
from keyboards.default.bosh_menu import til, bosh_menu, mahsulotlar
from keyboards.default.contact_button import contact_keyboard
from loader import dp


class RegState(StatesGroup):
    name = State()
    number = State()

# class Buyurtma(StatesGroup):
#     tavar = State()
#     middor = State()

# class Sentloco(StatesGroup):
#     loco = State()


@dp.message_handler(text="🏠Menyu")
async def bot_3422start(message: types.Message):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)

#
#
@dp.message_handler(text="🏠Menyu", state=[RegState.name, RegState.number])
async def bot_4324start(message: types.Message, state:FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)
    await state.finish()

#
#


#
#
@dp.message_handler(text="🏠Menyu", state=[Sentloco.loco])
async def bot_4242start(message: types.Message, state:FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)
    await state.finish()\



# @dp.message_handler(text="🏠Menyu")
# async def bot_43242rt(message: types.Message):
#     await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)
#
# #
# #
# @dp.message_handler(text="🏠Menyu", state=[RegState.name, RegState.number])
# async def bot_start(message: types.Message, state:FSMContext):
#     await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)
#     await state.finish()
#
# #
# #
#
#
#
#
@dp.message_handler(text="/start", state=[Sentloco.loco])
async def bot_st4234art(message: types.Message, state:FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)
    await state.finish()



@dp.message_handler(text="/start")
async def bo4242t_start(message: types.Message):
    user_id = message.from_user.id
    f = open("./data/reg/reklama.txt", "r")
    text = f.read()
    if not str(user_id) in text:
        f = open("./data/reg/reklama.txt", "a")
        f.write(f"{str(user_id)}\n")
    f.close()
    await message.answer(f"Assalomu Alaykum!", reply_markup=til)





@dp.message_handler(text="/start", state=[RegState.number, RegState.name])
async def bot_sa3242tarta(message: types.Message):
    await message.answer(f"Assalomu Alaykum!", reply_markup=til)

@dp.message_handler(text="🇺🇿 O'zbek")
async def bot_name(message: types.Message):
    user_id = message.from_user.id
    f = open("./data/reg/hammasi.txt", "r")
    text = f.read()
    f.close()
    if not str(user_id) in text:
        await message.answer(f"Ro'yxatdan o'rish uchun \n"
                             f"Ism Familyangizni kiriting.")
        await RegState.name.set()
    else:
        await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)


@dp.message_handler(state=RegState.name)
async def name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer(f"Kontaktingizni yuboring", reply_markup=contact_keyboard)
    await RegState.number.set()


@dp.message_handler(lambda message: message.text[:3]=="+998" and len(message.text)==13 , state=RegState.number)
async def con2131tact(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    number = message.contact.phone_number
    user_id = message.from_user.id

    h = open("./data/reg/hammasi.txt", "a")
    h.write(f"{user_id} {number} {name}\n")
    h.close()

    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(content_types="contact", state=RegState.number)
async def conta123ct(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    number = message.contact.phone_number
    user_id = message.from_user.id

    h = open("./data/reg/hammasi.txt", "a")
    h.write(f"\n{user_id} {number} {name}")
    h.close()

    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)
    await state.finish()




@dp.message_handler(text="📝 Mahsulotlar")
async def name(message: types.Message):
    await message.answer(f"Toifani tanlang", reply_markup=mahsulotlar)




@dp.message_handler(text="/help")
async def helpdads(message: types.Message):
    await message.answer(f"https://t.me/Coolprotec")
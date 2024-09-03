from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InputFile

from keyboards.default.bosh_menu import Fan, miqdor, buyutma, bosh_menu, mahsulotlar, buyutma_dastavka
from loader import dp
from utils.db_api.sqlite import Database

db = Database(path_to_db='./data/main.db')
try:
    db.create_table_users()
except:
    pass


class Buyurtma(StatesGroup):
    tavar = State()
    middor = State()

@dp.message_handler(text="🏠Menyu", state=[Buyurtma.tavar, Buyurtma.middor])
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text="Fan Coil")
async def tavar_8lar(message: types.Message):
    photo = InputFile('./data/photos/fan_koil.jpg')
    await message.answer_photo(photo, caption=f"💨 Shiftdagi konditsionerlar uchun ekranlar\n"
                                              f"💨 Himoya ekrani to'g'ridan-to'g'ri konditsioner havo oqimini aks ettiradi va tarqatadi\n"
                                              f"💨 Shaffof dizayn har qanday interyerga mos keladi\n"
                                              f"Narx:  65x65 450 000 so'mdan\n"
                                              f"        95x95 550 000 so'mdan\n",
                               reply_markup=Fan)


@dp.message_handler(text_contains="Fan Coil.")
async def tavar_8lar(message: types.Message, state: FSMContext):
    await state.update_data(
        {"tavar": message.text[-5:-3]}
    )
    await message.answer(f"👇🏻 Miqdorni tanlang yoki yozib qoldiring:", reply_markup=miqdor)
    await Buyurtma.tavar.set()


@dp.message_handler(text_contains="Konditsioner 7-12")
async def tavar_7lar(message: types.Message, state: FSMContext):
    await state.update_data(
        {"tavar": "7"}
    )
    photo = InputFile('./data/photos/7-12.jpg')
    await message.answer_photo(photo,
                               caption=f"💨 Devorga o'rnatilgan konditsionerlar uchun ekranlar 7 dan 12 gacha o'lchamdagi\n"
                                       f"💨 Himoya ekrani to'g'ridan-to'g'ri konditsioner havo oqimini aks ettiradi va tarqatadi\n"
                                       f"💨 Shaffof dizayn har qanday interyerga mos keladi\n"
                                       f"Narx: 150 000 so'mdan\n"
                                       f"👇🏻 Miqdorni tanlang yoki yozib qoldiring:", reply_markup=miqdor)
    await Buyurtma.tavar.set()


@dp.message_handler(text_contains="Konditsioner 18-24")
async def tavar_6lar(message: types.Message, state: FSMContext):
    await state.update_data(
        {"tavar": "18"}
    )
    photo = InputFile('./data/photos/18-24.jpg')
    await message.answer_photo(photo,
                               caption=f"💨 Devorga o'rnatilgan konditsionerlar uchun ekranlar 18 dan 24 gacha o'lchamdagi\n"
                                       f"💨 Himoya ekrani to'g'ridan-to'g'ri konditsioner havo oqimini aks ettiradi va tarqatadi\n"
                                       f"💨 Shaffof dizayn har qanday interyerga mos keladi\n"
                                        f"Narx: 200 000 so'mdan\n"
                                       f"👇🏻 Miqdorni tanlang yoki yozib qoldiring:", reply_markup=miqdor)
    await Buyurtma.tavar.set()


@dp.message_handler(text_contains="Konditsioner 36-48")
async def tavar_5lar(message: types.Message, state: FSMContext):
    await state.update_data(
        {"tavar": "36"}
    )
    photo = InputFile('./data/photos/18-24.jpg')
    await message.answer_photo(photo,
                               caption=f"💨 Devorga o'rnatilgan konditsionerlar uchun ekranlar 36 dan 48 gacha o'lchamdagi\n"
                                       f"💨 Himoya ekrani to'g'ridan-to'g'ri konditsioner havo oqimini aks ettiradi va tarqatadi\n"
                                       f"💨 Shaffof dizayn har qanday interyerga mos keladi\n"                                       
                                       f"Narx: 300 000 so'mdan\n"
                                       f"👇🏻 Miqdorni tanlang yoki yozib qoldiring:", reply_markup=miqdor)
    await Buyurtma.tavar.set()


# State miqdor
@dp.message_handler(lambda message: message.text.isdigit(), state=Buyurtma.tavar)
async def miqsqaasdor(message: types.Message, state: FSMContext):
    data = await state.get_data()
    tavar = str(data.get("tavar"))
    miqdor = message.text
    # tavar_tayyor = "kon"+tavar

    user = db.select_user(user_id=message.from_user.id)
    if not user:
        user = db.add_user(user_id=message.from_user.id)

    t7 = 0
    t18 = 0
    t36 = 0
    t65 = 0
    t95 = 0

    if tavar == "7":
        t7 = miqdor
        db.update_user_kon7(user_id=message.from_user.id, kon7=str(miqdor))
    if tavar == "18":
        t18 = miqdor
        db.update_user_kon18(user_id=message.from_user.id, kon18=str(miqdor))
    if tavar == "36":
        t36 = miqdor
        db.update_user_kon36(user_id=message.from_user.id, kon36=str(miqdor))
    if tavar == "65":
        t65 = miqdor
        db.update_user_kon65(user_id=message.from_user.id, kon65=str(miqdor))
    if tavar == "95":
        t95 = miqdor
        db.update_user_kon95(user_id=message.from_user.id, kon95=str(miqdor))
    user = db.select_user(user_id=message.from_user.id)
    kon7 = user[2]
    kon18 = user[3]
    kon36 = user[4]
    kon65 = user[5]
    kon95 = user[6]

    tavar = ""
    summ = 0
    if kon7:
        tavar = tavar+f"Konditsioner 7-12 :  {kon7} dona  {int(kon7)*140000} so'm\n"
        summ = summ + int(kon7)*140000
    if kon18:
        tavar = tavar+f"Konditsioner 18-24 :  {kon18} dona  {int(kon18)*190000} so'm\n"
        summ = summ + int(kon18)*190000

    if kon36:
        tavar = tavar+f"Konditsioner 36-48 :  {kon36} dona  {int(kon36)*300000} so'm\n"
        summ = summ + int(kon36)*300000

    if kon65:
        tavar = tavar+f"Fan Coil. 65-65 :  {kon65} dona  {int(kon65)*450000} so'm\n"
        summ = summ + int(kon65)*450000

    if kon95:
        tavar = tavar+f"Fan Coil. 95-95 :  {kon95} dona  {int(kon95)*550000} so'm\n"
        summ = summ + int(kon95)*550000

    await message.answer(f"Buyutmalaringiz:\n"
                         f"{tavar}\n"
                         f"jami narx : {summ} so'mlik")
    await message.answer(f"Sizning buyurtmagiz savatga joylandi", reply_markup=buyutma)
    await state.finish()


@dp.message_handler(lambda message: not message.text.isdigit(), state=Buyurtma.tavar)
async def miqdor_not(message: types.Message):
    return await message.answer(F"Iltimos bu yerga faqat raqam yuboring")


@dp.message_handler(text="📝Buyurtma qo'shish")
async def mi321or(message: types.Message, state: FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=mahsulotlar)


@dp.message_handler(text="🔄Savatni tozalash")
async def mi321or(message: types.Message, state: FSMContext):
    db.update_user_kon7(user_id=message.from_user.id, kon7=None)
    db.update_user_kon18(user_id=message.from_user.id, kon18=None)
    db.update_user_kon36(user_id=message.from_user.id, kon36=None)
    db.update_user_kon65(user_id=message.from_user.id, kon65=None)
    db.update_user_kon95(user_id=message.from_user.id, kon95=None)
    await message.answer(f"Savat tozalandi", reply_markup=bosh_menu)


@dp.message_handler(text="🛒 Savat")
async def mi1r(message: types.Message, state: FSMContext):
    user = db.select_user(user_id=message.from_user.id)
    if not user:
        user = db.add_user(user_id=message.from_user.id)

    kon7 = user[2]
    kon18 = user[3]
    kon36 = user[4]
    kon65 = user[5]
    kon95 = user[6]
    tavar = ""
    summ = 0
    if kon7:
        tavar = tavar+f"Konditsioner 7-12 :  {kon7} dona  {int(kon7)*140000} so'm\n"
        summ = summ + int(kon7)*140000
    if kon18:
        tavar = tavar+f"Konditsioner 18-24 :  {kon18} dona  {int(kon18)*190000} so'm\n"
        summ = summ + int(kon18)*190000

    if kon36:
        tavar = tavar+f"Konditsioner 36-48 :  {kon36} dona  {int(kon36)*300000} so'm\n"
        summ = summ + int(kon36)*300000

    if kon65:
        tavar = tavar+f"Fan Coil. 65-65 :  {kon65} dona  {int(kon65)*450000} so'm\n"
        summ = summ + int(kon65)*450000

    if kon95:
        tavar = tavar+f"Fan Coil. 95-95 :  {kon95} dona  {int(kon95)*550000} so'm\n"
        summ = summ + int(kon95)*550000

    await message.answer(f"Buyutmalaringiz:\n"
                         f"{tavar}\n"
                         f"jami narx : {summ} so'mlik", reply_markup=buyutma)

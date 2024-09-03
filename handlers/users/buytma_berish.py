from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users import functions
from handlers.users.tavar import db
from keyboards.default.bosh_menu import buyutma_dastavka, bosh_menu, loco_keyboard, mahsulotlar
from loader import dp, bot


@dp.message_handler(text="✅Buyurtmani amalga oshirish")
async def mi23424or(message: types.Message, state: FSMContext):
    await message.answer(f"Kerakli bo'limni tanlang", reply_markup=buyutma_dastavka)


@dp.message_handler(text="🚶‍♂Olib ketish")
async def bot32414o(message: types.Message):
    lat1 = 41.286857
    lon1 = 69.184952
    lat2 = 41.293082
    lon2 = 69.356471
    number = functions.find_nomer(str(message.from_user.id))
    await message.answer_location(latitude=lat1,
                                  longitude=lon1)
    await message.answer(f"Chilonzor tumani, Farxod bozori (Lola perfumery)")
    await message.answer_location(latitude=lat2,
                                  longitude=lon2)
    await message.answer(f"Yashnobod tumani, 40 let pobeda, Krestik (Jayxun foto)", reply_markup=bosh_menu)

    user = db.select_user(user_id=message.from_user.id)
    kon7 = user[2]
    kon18 = user[3]
    kon36 = user[4]
    kon65 = user[5]
    kon95 = user[6]
    tavar  =" "
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

    db.update_user_kon7(user_id=message.from_user.id, kon7=None)
    db.update_user_kon18(user_id=message.from_user.id, kon18=None)
    db.update_user_kon36(user_id=message.from_user.id, kon36=None)
    db.update_user_kon65(user_id=message.from_user.id, kon65=None)
    db.update_user_kon95(user_id=message.from_user.id, kon95=None)

    await bot.send_message(chat_id=-4142834280, text=f"🙎🏻‍♂️Mijoz : {message.from_user.full_name}\n"
                                                     f"📲Phone number : {number}\n"
                                                     f"Username : @{message.from_user.username}\n"
                                                     f"🚶‍♂Olib ketish\n"
                                                     f"{tavar} \njami narx : {summ} so'mlik")


class Sentloco(StatesGroup):
    loco = State()


# @dp.message_handler(content_types="location")
# async def handle_location(message: types.Message):
#     lat = message.location.latitude
#     lon = message.location.longitude
#     print(lat)
#     print(lon)


@dp.message_handler(text= "📲Yandeksdan yetkazish (1 soat ichida)")
async def lo423424co(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(
        {"yet_tur": msg}
    )
    await message.answer(f"Locatsiyangizni yuboring", reply_markup=loco_keyboard)
    await Sentloco.loco.set()


@dp.message_handler(text="⚙Yetkazish va o'rnatib berish (1 kun ichida)")
async def l42342oco(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(
        {"yet_tur": msg}
    )
    await message.answer(f"Locatsiyangizni yuboring", reply_markup=loco_keyboard)
    await Sentloco.loco.set()


@dp.message_handler(content_types="location", state=Sentloco.loco)
async def qabulloco(message: types.Message, state: FSMContext):

    lat = message.location.latitude
    lon = message.location.longitude
    number = functions.find_nomer(str(message.from_user.id))
    # print(lat)
    # print(lon)
    data = await state.get_data()
    yet_tur = data.get("yet_tur")
    user = db.select_user(user_id=message.from_user.id)
    kon7 = user[2]
    kon18 = user[3]
    kon36 = user[4]
    kon65 = user[5]
    kon95 = user[6]
    tavar  =" "
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

    db.update_user_kon7(user_id=message.from_user.id, kon7=None)
    db.update_user_kon18(user_id=message.from_user.id, kon18=None)
    db.update_user_kon36(user_id=message.from_user.id, kon36=None)
    db.update_user_kon65(user_id=message.from_user.id, kon65=None)
    db.update_user_kon95(user_id=message.from_user.id, kon95=None)

    await message.answer(f"Sizning so'rovingiz qabul qilindi\n"
                         f"Tez orada xodimlarimiz siz bilan bog'lanishadi", reply_markup=bosh_menu)
    if yet_tur == "📲Yandeksdan yetkazish (1 soat ichida)":

        await bot.send_message(chat_id=-4119351805, text=f"🙎🏻‍♂️Mijoz : {message.from_user.full_name}\n"
                                                         f"📲Phone number : +{number}\n"
                                                         f"Username : @{message.from_user.username}\n"
                                                         f"📲Yandeksdan yetkazish\n"
                                                         f"{tavar}\n jami narx : {summ} so'mlik")
        await bot.send_location(chat_id=-4119351805, latitude=lat, longitude=lon)
    else:

        await bot.send_message(chat_id=-4199441276, text=f"🙎🏻‍♂️Mijoz : {message.from_user.full_name}\n"
                                                         f"📲Phone number : +{number}\n"
                                                         f"Username : @{message.from_user.username}\n"
                                                         f"⚙Yetkazish va o'rnatib berish\nDastavka: 50000 so'm\n"
                                                         f"{tavar}\n jami narx : {summ+50000} so'mlik")
        await bot.send_location(chat_id=-4199441276, latitude=lat, longitude=lon)
    await state.finish()

#
# @dp.message_handler(state=Sentloco.loco)
# async def qab123u(message: types.Message, state: FSMContext):
#     return await message.answer(f"Просто введите свое местоположение: ")

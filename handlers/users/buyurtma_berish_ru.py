from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from handlers.users import functions
from handlers.users.tavar import db

from keyboards.default.bosh_menu_ru import buyutma_dastavka_ru, loco_keyboard_ru, bosh_menu_ru
from loader import dp, bot


@dp.message_handler(text="✅ Завершение заказа")
async def mi23424or_ru(message: types.Message, state: FSMContext):
    await message.answer(f"Выберите нужный раздел", reply_markup=buyutma_dastavka_ru)


@dp.message_handler(text="🚶‍♂Самовывоз")
async def bot32414o_ru(message: types.Message):
    lat1 = 41.286857
    lon1 = 69.184952
    lat2 = 41.293082
    lon2 = 69.356471
    number = functions.find_nomer(str(message.from_user.id))
    await message.answer_location(latitude=lat1,
                                  longitude=lon1)
    await message.answer(f'Чиланзарский район, Фархадский рынок, Парфюмерный магазин "Lola"')
    await message.answer_location(latitude=lat2,
                                  longitude=lon2)
    await message.answer(f"Яшнабад район, 40 лет победы, Крестик (фото Джейхуна)", reply_markup=bosh_menu_ru)

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

    await bot.send_message(chat_id=-4142834280, text=f"🙎🏻‍♂️Mijoz : {message.from_user.full_name}\n"
                                                     f"📲Phone number : {number}\n"
                                                     f"Username : @{message.from_user.username}\n"
                                                     f"🚶‍♂Olib ketish\n"
                                                     f"{tavar}\n jami narx : {summ} so'mlik")


class Sentloco_ru(StatesGroup):
    loco = State()


# @dp.message_handler(content_types="location")
# async def handle_location(message: types.Message):
#     lat = message.location.latitude
#     lon = message.location.longitude
#     print(lat)
#     print(lon)


@dp.message_handler(text= "📲 Доставка через Яндкс (менее 1 часа)")
async def lo42342432o_ru(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(
        {"yet_turi": msg}
    )
    await message.answer(f"Отправьте свое местоположение", reply_markup=loco_keyboard_ru)
    await Sentloco_ru.loco.set()


@dp.message_handler(text="⚙Доставка и установка (менее 1 дня)")
async def l42342o2342o(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(
        {"yet_turi": msg}
    )
    await message.answer(f"Отправьте свое местоположение", reply_markup=loco_keyboard_ru)
    await Sentloco_ru.loco.set()


@dp.message_handler(content_types="location", state=Sentloco_ru.loco)
async def qabul2432u(message: types.Message, state: FSMContext):
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

    await message.answer(f"Ваш запрос принят\n"
                          f"Наши сотрудники свяжутся с вами в ближайшее время", reply_markup=bosh_menu_ru)
    if yet_tur == "📲 Доставка через Яндкс (менее 1 часа)":

        await bot.send_message(chat_id=-4119351805, text=f"🙎🏻‍♂️Mijoz : {message.from_user.full_name}\n"
                                                         f"📲Phone number : +{number}\n"
                                                         f"Username : @{message.from_user.username}\n"
                                                         f"📲 Доставка через Яндкс\n"
                                                         f"{tavar}\n jami narx : {summ} so'mlik")
        await bot.send_location(chat_id=-4119351805, latitude=lat, longitude=lon)
    else:

        await bot.send_message(chat_id=-4199441276, text=f"🙎🏻‍♂️Mijoz : {message.from_user.full_name}\n"
                                                         f"📲Phone number : +{number}\n"
                                                         f"Username : @{message.from_user.username}\n"
                                                         f"⚙Доставка и установка \nДоставка : 50000 cум "
                                                         f"{tavar}\n jami narx : {summ+50000} so'mlik")
        await bot.send_location(chat_id=-4199441276, latitude=lat, longitude=lon)
    await state.finish()
    
    
# @dp.message_handler(state=Sentloco_ru.loco)
# async def qab1231_ru(message: types.Message, state: FSMContext):
#     return await message.answer(f"Просто введите свое местоположение: ")


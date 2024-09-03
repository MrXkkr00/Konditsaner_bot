from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InputFile

from keyboards.default.bosh_menu_ru import Fan_ru, miqdor_ru, buyutma_ru, mahsulotlar_ru, bosh_menu_ru
from loader import dp
from utils.db_api.sqlite import Database

db = Database(path_to_db='./data/main.db')
try:
    db.create_table_users()
except:
    pass



class Buyurtma_ru(StatesGroup):
    tavar = State()
    middor = State()

@dp.message_handler(text="🏠Меню", state=[Buyurtma_ru.tavar, Buyurtma_ru.middor])
async def bot_ru_start(message: types.Message, state:FSMContext):
    await message.answer(f"Выберите нужный раздел", reply_markup=bosh_menu_ru)
    await state.finish()


@dp.message_handler(text="Фан койл")
async def tavarru_4lar(message: types.Message):
    photo = InputFile('./data/photos/fan_koil.jpg')
    await message.answer_photo(photo, caption=f"💨 Экраны для потолочных кондиционеров\n"
                                              f"💨 Защитный экран отражает и рассеивает прямые потоки "
                                              f"кондиционированного воздуха\n "
                                              f"💨 Прозрачная конструкция подойдёт под любой интерьер\n"
                                              f"цена:  65x65 450 000 сум\n"
                                              f"        95x95 550 000 сум", reply_markup=Fan_ru)

@dp.message_handler(text_contains="Фан койл.")
async def tavar_8lar(message: types.Message, state: FSMContext):
    await state.update_data(
        {"tavar": message.text[-5:-3]}
    )
    await message.answer(f"👇🏻 Выберите или напишите сумму:", reply_markup=miqdor_ru)
    await Buyurtma_ru.tavar.set()


@dp.message_handler(text_contains="Кондиционер 7-12")
async def tavar_3lruar(message: types.Message, state: FSMContext):
    await state.update_data(
        {"tavar": "7"}
    )
    photo = InputFile('./data/photos/7-12.jpg')
    await message.answer_photo(photo, caption=f"💨 Экраны для настенных кондиционеров от 7 до 12го размера\n"
                                              f"💨 Защитный экран отражает и рассеивает прямые потоки "
                                              f"кондиционированного воздуха\n "
                                              f"💨 Прозрачная конструкция подойдёт под любой интерьер\n"
                                              f"цена: 150 000 сум", reply_markup=miqdor_ru)
    await Buyurtma_ru.tavar.set()





@dp.message_handler(text_contains="Кондиционер 18-24")
async def tavar_2lruar(message: types.Message, state:FSMContext):
    await state.update_data(
        {"tavar": "18"}
    )
    photo = InputFile('./data/photos/18-24.jpg')
    await message.answer_photo(photo, caption=f"💨 Экраны для настенных кондиционеров от 18 до 24го размера\n"
                                              f"💨 Защитный экран отражает и рассеивает прямые потоки "
                                              f"кондиционированного воздуха\n "
                                              f"💨 Прозрачная конструкция подойдёт под любой интерьер\n"
                                              f"цена: 200 000 сум\n"
                                              f"👇🏻 Выберите количество или запиши это:", reply_markup=miqdor_ru)
    await Buyurtma_ru.tavar.set()



@dp.message_handler(text_contains="Кондиционер 36-48")
async def tavarruar(message: types.Message, state:FSMContext):
    await state.update_data(
        {"tavar": "36"}
    )
    photo = InputFile('./data/photos/36-24.jpg')
    await message.answer_photo(photo, caption=f"💨 Экраны для настенных кондиционеров от 36 до 48го размера\n"
                                              f"💨 Защитный экран отражает и рассеивает прямые потоки "
                                              f"кондиционированного воздуха\n "
                                              f"💨 Прозрачная конструкция подойдёт под любой интерьер\n"
                                              f"цена: 350 000 сум\n"
                                              f"👇🏻 Выберите количество или запиши это:", reply_markup=miqdor_ru)
    await Buyurtma_ru.tavar.set()





# State miqdor
@dp.message_handler(lambda message: message.text.isdigit(), state=Buyurtma_ru.tavar)
async def miqsqaasdor_ru(message: types.Message, state: FSMContext):
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
        tavar = tavar+f"Кондиционер 7-12 :  {kon7}  шт. {int(kon7)*140000} сум\n"
        summ = summ + int(kon7)*140000
    if kon18:
        tavar = tavar+f"Кондиционер 18-24 :  {kon18} шт.  {int(kon18)*190000} сум\n"
        summ = summ + int(kon18)*190000

    if kon36:
        tavar = tavar+f"Кондиционер 36-48 :  {kon36} шт.  {int(kon36)*300000} сум\n"
        summ = summ + int(kon36)*300000

    if kon65:
        tavar = tavar+f"Фан койл. 65-65 :  {kon65}  шт. {int(kon65)*450000} сум\n"
        summ = summ + int(kon65)*450000

    if kon95:
        tavar = tavar+f"Фан койл. 95-95 :  {kon95} шт.  {int(kon95)*550000} сум\n"
        summ = summ + int(kon95)*550000
    await message.answer(f"Ваши измерения:\n"
                         f"{tavar}\nитого : {summ} сум")
    await message.answer(f"Ваш заказ помещен в корзину", reply_markup=buyutma_ru)
    await state.finish()


@dp.message_handler(lambda message: not message.text.isdigit(), state=Buyurtma_ru.tavar)
async def miqdor_not_ru(message: types.Message):
    return await message.answer(F"Пожалуйста, пришлите сюда только номер")


@dp.message_handler(text="📝Добавить заказ")
async def mi321or_ru(message: types.Message, state: FSMContext):
    await message.answer(f"Выберите нужный раздел", reply_markup=mahsulotlar_ru)


@dp.message_handler(text="🔄Очистить корзину")
async def mi321or_ru(message: types.Message, state: FSMContext):
    db.update_user_kon7(user_id=message.from_user.id, kon7=None)
    db.update_user_kon18(user_id=message.from_user.id, kon18=None)
    db.update_user_kon36(user_id=message.from_user.id, kon36=None)
    db.update_user_kon65(user_id=message.from_user.id, kon65=None)
    db.update_user_kon95(user_id=message.from_user.id, kon95=None)
    await message.answer(f"Корзина очищена", reply_markup=bosh_menu_ru)


@dp.message_handler(text="🛒 Корзина")
async def mi1r_ru(message: types.Message, state: FSMContext):
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
        tavar = tavar+f"Кондиционер 7-12 :  {kon7}  шт. {int(kon7)*140000} сум\n"
        summ = summ + int(kon7)*140000
    if kon18:
        tavar = tavar+f"Кондиционер 18-24 :  {kon18}  шт. {int(kon18)*190000} сум\n"
        summ = summ + int(kon18)*190000

    if kon36:
        tavar = tavar+f"Кондиционер 36-48 :  {kon36} шт.  {int(kon36)*300000} сум\n"
        summ = summ + int(kon36)*300000

    if kon65:
        tavar = tavar+f"Фан койл. 65-65 :  {kon65} шт.  {int(kon65)*450000} сум\n"
        summ = summ + int(kon65)*450000

    if kon95:
        tavar = tavar+f"Фан койл. 95-95 :  {kon95}  шт. {int(kon95)*550000} сум\n"
        summ = summ + int(kon95)*550000

    await message.answer(f"Ваши измерения:\n"
                         f"{tavar}\n"
                         f"итого : {summ} сум", reply_markup=buyutma_ru)



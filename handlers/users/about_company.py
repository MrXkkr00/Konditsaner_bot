from aiogram import types

from loader import dp


@dp.message_handler(text="🏢Biz haqimizda")
async def bot_start(message: types.Message):
    await message.answer(f"2021 yildan bizning Coolprotec jamoasi har biringizni"
                         f"himoyalangan his qilish uchun ofis va uy uchun plastik ekranlar "
                         f"ishlab chiqaradi.\n\n"

                        f"Barcha turdagi konditsionerlar uchun himoya ekranlar ishlab "
                         f"chiqaramiz. Bu shamollashdan oddiy va samarali himoya! "
                         f"U kondisioner ostida o'rnatiladi va sovuq havoni to'g'rilash uchun "
                         f"mo'ljallangan, shu bilan birga uni xona bo'ylab teng taqsimlaydi."
                         f" Odamga to'g'ridan-to'g'ri havo oqimidan himoya qiladi.\n\n"
                         f"Dillerlikga ham  taklif qilamiz\n"
                         f"+998331234533\n"
                         f"+998935888831\n"
                         f"@coolprotec")



@dp.message_handler(text="🏢 О нас")
async def bot_start(message: types.Message):
    await message.answer(f"С 2021 года мы команда Coolprotec производим пластиковые экраны для "
                         f"офиса и дома, чтобы каждый из вас чувствовал себя защищенным.\n\n"

                        f"Защитные экраны для всех видов кондиционеров. Это простая и эффективная защита от простуды!\n"
                         f"Устанавливается под внутренним блоком и предназначен для корректировки холодного воздуха, "
                         f"при этом равномерно распределяя его по всему помещению.\n"
                         f"Защищает от прямого попадания воздушных потоков на человека.\n\n"
                         f"Мы также предлагаем дилерство\n"
                         f"+998331234533\n"
                         f"+998935888831\n"
                         f"@coolprotec")

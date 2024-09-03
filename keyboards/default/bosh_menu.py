from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Mahsulotlar"),
        ],
        [
            KeyboardButton(text='🏢Biz haqimizda'),
            KeyboardButton(text="🛒 Savat"),
        ],

    ],
    resize_keyboard=True
)




til = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbek"),
            KeyboardButton(text="🇷🇺 Русский"),
        ]
    ], resize_keyboard=True
)

mahsulotlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Konditsioner 7-12"),
            KeyboardButton(text="Konditsioner 18-24"),
        ],
        [
            KeyboardButton(text="Konditsioner 36-48"),
            KeyboardButton(text="Fan Coil"),
        ],
        [
            KeyboardButton(text="🏠Menyu")
        ]
    ], resize_keyboard=True
)


Fan = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fan Coil. 65-65"),
        ],
        [
            KeyboardButton(text="Fan Coil. 95-95"),
        ],
        [
            KeyboardButton(text="🏠Menyu")
        ]
    ], resize_keyboard=True
)



miqdor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
        ],
        [
            KeyboardButton(text="6"),
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9"),
            KeyboardButton(text="10"),
        ],
        [
            KeyboardButton(text="🏠Menyu")
        ]
    ], resize_keyboard=True
)



buyutma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅Buyurtmani amalga oshirish"),
        ],
        [
            KeyboardButton(text="📝Buyurtma qo'shish"),
        ],
        [
            KeyboardButton(text="🔄Savatni tozalash"),
        ],
        [
            KeyboardButton(text="🏠Menyu")
        ]
    ], resize_keyboard=True
)


buyutma_dastavka = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚶‍♂Olib ketish"),
        ],
        [
            KeyboardButton(text="⚙Yetkazish va o'rnatib berish (1 kun ichida)"),
        ],
        [
            KeyboardButton(text="📲Yandeksdan yetkazish (1 soat ichida)"),
        ],
        [
            KeyboardButton(text="🏠Menyu")
        ]
    ], resize_keyboard=True
)

loco_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📍location",
                                                      request_location=True)
                                   ],
                                   [
                                       KeyboardButton(text="🏠Menyu")
                                   ]
                               ])

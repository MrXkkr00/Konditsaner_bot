from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bosh_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Продукты"),
        ],
        [
            KeyboardButton(text='🏢 О нас'),
            KeyboardButton(text="🛒 Корзина"),
        ],

    ],
    resize_keyboard=True
)


mahsulotlar_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кондиционер 7-12"),
            KeyboardButton(text="Кондиционер 18-24"),
        ],
        [
            KeyboardButton(text="Кондиционер 36-48"),
            KeyboardButton(text="Фан койл"),
        ],
        [
            KeyboardButton(text="🏠Меню")
        ]
    ], resize_keyboard=True
)

Fan_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Фан койл. 65-65"),
        ],
        [
            KeyboardButton(text="Фан койл. 95-95"),
        ],
        [
            KeyboardButton(text="🏠Menyu")
        ]
    ], resize_keyboard=True
)



miqdor_ru = ReplyKeyboardMarkup(
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
            KeyboardButton(text="🏠Меню")
        ]
    ], resize_keyboard=True
)

buyutma_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Завершение заказа"),
        ],
        [
            KeyboardButton(text="📝Добавить заказ"),
        ],
        [
            KeyboardButton(text="🔄Очистить корзину"),
        ],
        [
            KeyboardButton(text="🏠Меню")
        ]
    ], resize_keyboard=True
)

buyutma_dastavka_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚶‍♂Самовывоз"),
        ],
        [
            KeyboardButton(text="⚙Доставка и установка (менее 1 дня)"),
        ],
        [
            KeyboardButton(text="📲 Доставка через Яндкс (менее 1 часа)"),
        ],
        [
            KeyboardButton(text="🏠Меню")
        ]
    ], resize_keyboard=True
)


loco_keyboard_ru = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📍местоположение",
                                                      request_location=True)
                                   ],
                                   [
                                       KeyboardButton(text="🏠Меню")
                                   ]
                               ])
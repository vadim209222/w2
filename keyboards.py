from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import (
    ReplyKeyboardMarkup,  #клавиатура которая крепится под полем ввода
    KeyboardButton,        #кнопка для клавиатуры выше
    InlineKeyboardMarkup,   #клавиатура которая крепится под сообщениями
    InlineKeyboardButton      #кнопка для клавиатуры выше
)

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Присоединиться', callback_data='join')
        ],
        [
            InlineKeyboardButton(text='Публичная оферта', web_app=WebAppInfo(url='https://vrbank.ru/docs/7.pdf'))
        ]
    ],
    resize_keyboard=True,  # размер кнопок адаптирован под тел
    one_time_keyboard=True,  # кнопки после нажатия не скрываются
)

links_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Поделиться контактом', request_contact=True)
        ]
    ],
    resize_keyboard=True,  # размер кнопок адаптирован под тел
    one_time_keyboard=True,  # кнопки после нажатия не скрываются
)


payment_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=' Подписка на 30 дней', web_app=WebAppInfo(url='https://payform.ru/6q3SvlC/'))
        ],
        [
            InlineKeyboardButton(text='Отменить подписку', web_app=WebAppInfo(url='https://yourbodymind.ru/page47446555.html'))
        ]
    ]

)



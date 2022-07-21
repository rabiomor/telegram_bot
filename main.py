
import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
from cred import TOKEN
from menu import main_menu_keyboard, service_menu_keyboard
from key_buttons import tele_button, service

def start(update:  Update, context: CallbackContext):
     context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgEAAxkBAAEFQoNizpTzIgNa2KaLRd-LymIAATyhIm4AAvQAA9Yvmwa8C9oBgOI1IikE'
    ) 
     update.message.reply_text(
        '👋Добро  пожаловать, {username}.\nВас  приветсвует  салон  красоты  𝐀𝐫𝐬𝐚𝐲𝐚𝐧𝐁𝐞𝐚𝐮𝐭𝐲😊'.format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user
        ),
             reply_markup=main_menu_keyboard()             
    )

def back(update:  Update, context: CallbackContext):
    update.message.reply_text(
        'Вы  в  главном  меню',
        reply_markup=main_menu_keyboard()             
    )

# ONAS = r'(?=('+(tele_button[0])+r'))'
SERVICE_RAGEX = r'(?=('+(tele_button[0])+r'))'
ZAPIS =  r'(?=('+(tele_button[2])+r'))'
LOCATION = r'(?=('+(tele_button[1])+r'))'

NAILS_REGEX = r'(?=('+(service[0])+r'))'
MAKEUP_REGEX = r'(?=('+(service[1])+r'))'
LASHES_REGEX = r'(?=('+(service[2])+r'))'
HAIR_REGEX = r'(?=('+(service[3])+r'))'
BACK_KEY = r'(?=('+(service[4])+r'))'

def zapisat(update: Update, context: CallbackContext):  
    z = update.message.text
    if z[:6] == 'Запись':   
         context.bot.send_message(
            chat_id= '',
            text = z
        )

def resive_info(update:Update, context: CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of 𝐀𝐫𝐬𝐚𝐲𝐚𝐧𝐁𝐞𝐚𝐮𝐭𝐲'
    )
    update.message.reply_location(
        # '42.86947692066429, 74.61498334767985'
        longitude=74.61498334767985,
        latitude=42.86947692066429,
        reply_to_message_id=msg.message_id 

    )



def resive_service_menu(update:Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите  услуги😊',
        reply_markup=service_menu_keyboard()
    )
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFOWRiyBYAAVRli6yP9mVH8vx0cpPjuQcAArJ3AQABY4tGDAH_DeHCob-BKQQ'
    ) 


def resive_info(update:Update, context: CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = '📍Location of 𝐀𝐫𝐬𝐚𝐲𝐚𝐧𝐁𝐞𝐚𝐮𝐭𝐲📍'
    )
    update.message.reply_location(
        # 42.85279408999205, 

        longitude=74.60947502145646,
        latitude=42.85279408999205,
        reply_to_message_id=msg.message_id 

    )
def zapis(update: Update, context: CallbackContext):
    info = re.match(ZAPIS, update.message.text)
    update.message.reply_text(
    text = """
1. Напишите  ваше  имя.
2. Ваш  номер  телефона.
После  отправки  всех  заполненных  бланок
Админ  вам  позвонит!

А  так  же  наш  𝐖𝐡𝐚𝐭𝐬𝐀𝐚𝐩𝐩
⬇️⬇️⬇️

https://l.instagram.com/?u=https%3A%2F%2Fwa.me%2F996505120592&e=ATPqQqACzr0HN1g7JrApMMyaG_dEDBKyD8k2Ynj8mNPx4XKiexP0C6pFRNp1lcQhf78c3_gC6lGxM4wTWw3oNg&s=1
""" 
)
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgEAAxkBAAEFOVpiyBQIFQ9QhMQZRiFeWGTdPlAigwAC9AAD1i-bBrwL2gGA4jUiKQQ'
    )

    
def nails_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Мастер', callback_data='nails_master'),
            InlineKeyboardButton('Прайс', callback_data='nails_price'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите  опцию😊',
        reply_markup=reply_markup
    )


def makeup_inline_menu(update: Update, context: CallbackContext):
    keyboard_makeup = [
        [
            InlineKeyboardButton('Мастер', callback_data='makeup_master'),
            InlineKeyboardButton('Прайс', callback_data='makeup_price')

        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_makeup)
    update.message.reply_text(
        'Выберите  опцию😊',
        reply_markup=reply_markup
    )

def lashes_inline_menu(update: Update, context: CallbackContext):
    keyboard_lashes = [
        [
            InlineKeyboardButton('Мастер', callback_data='lashes_master'),
            InlineKeyboardButton('Прайс', callback_data='lashes_price'),

]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_lashes)
    update.message.reply_text(
        'Выберите  опцию😊',
        reply_markup=reply_markup
    )


def hair_inline_menu(update: Update, context: CallbackContext):
    keyboard_hair = [
        [
            InlineKeyboardButton('Мастер', callback_data='hair_master'),
            InlineKeyboardButton('Прайс', callback_data='hair_price'),

]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_hair)
    update.message.reply_text(
        'Выберите  опцию😊',
        reply_markup=reply_markup
    )


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'nails_master':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/as.jpg', 'rb'),
            caption = '''
Имя:  Томирис
Возраст:  2️⃣1️⃣ 
Опыт работы:  5️⃣  лет
            '''
        )

    if query.data == 'nails_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Маникюр  с  покрытием - 8️⃣0️⃣0️⃣с
Наращивание  ногтей - 1️⃣0️⃣0️⃣0️⃣с
Классический  маникюр - 3️⃣5️⃣0️⃣с


                '''
            )
  
    if query.data == 'makeup_master':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/sa.jpg', 'rb'),
            caption = '''
Имя:   Арсаяна
Возраст:  2️⃣3️⃣
Опыт работы:  2️⃣  года
            '''
        )


    if query.data == 'makeup_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Макияж  дневной - 1️⃣2️⃣0️⃣0️⃣с
Макияж  вечерний - 1️⃣5️⃣0️⃣0️⃣с
                '''
            )

    if query.data == 'lashes_master':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ka.jpg', 'rb'),
            caption = '''
Имя:  Аделина
Возраст:  2️⃣4️⃣
Опыт работы:  3️⃣  года
            '''
        )


    if query.data == 'lashes_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
1d - 1️⃣0️⃣0️⃣0️⃣c
2d -  1️⃣2️⃣0️⃣0️⃣c
3d - 1️⃣3️⃣0️⃣0️⃣c
4d - 5d - 1️⃣5️⃣0️⃣0️⃣c
                '''
            )

    if query.data == 'hair_master':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ma.jpg', 'rb'),
            caption = '''
Имя:  Тилекмат
Возраст:  2️⃣0️⃣
Опыт работы:  2️⃣  года
            '''
        )

    if query.data == 'hair_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = '''
Стрижка  от  5️⃣0️⃣0️⃣с
Укладка - 5️⃣0️⃣0️⃣с
Сложное  окрашивание  от  2️⃣0️⃣0️⃣0️⃣с
Прически  от  1️⃣0️⃣0️⃣0️⃣с
                '''
            )


            

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot-data'))
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(SERVICE_RAGEX),
    resive_service_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    resive_info
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(NAILS_REGEX),
    nails_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LASHES_REGEX),
    lashes_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MAKEUP_REGEX),
    makeup_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HAIR_REGEX),
    hair_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_KEY),
    start
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_KEY),
    main_menu_keyboard
))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ZAPIS),
    zapis
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zapisat
))

updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()
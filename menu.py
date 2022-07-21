import telegram
from key_buttons import tele_button, service

def main_menu_keyboard():
    keyboard = ([
            [telegram.KeyboardButton(tele_button[0]),],
            [telegram.KeyboardButton(tele_button[1])],
            [telegram.KeyboardButton(tele_button[2]),],
            # [telegram.KeyboardButton(tele_button[3]),],

    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def service_menu_keyboard():
    keyboard = ([
            [telegram.KeyboardButton(service[0]),],
            [telegram.KeyboardButton(service[1])],
            [telegram.KeyboardButton(service[2]),],
            [telegram.KeyboardButton(service[3]),],     
            [telegram.KeyboardButton(service[4]),],     

    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


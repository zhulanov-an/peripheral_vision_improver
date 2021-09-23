from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup

import settings


def get_emoji(user_data):
    if "emoji" not in user_data:
        smile = choice(settings.USER_EMOJI)
        smile = emojize(smile, use_aliases=True)
        user_data["emoji"] = smile
    return user_data["emoji"]


def get_keyboard():
    # TODO сделать полуяение из .env, но нужно разобраться с load_env vs import
    # как сделать так, что импорт начинается после загрузки переменных среды?
    return ReplyKeyboardMarkup([["/shulte 3", "/shulte 5", "/shulte 7"]])
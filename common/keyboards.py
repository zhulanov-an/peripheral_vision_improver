from telegram import ReplyKeyboardMarkup


def get_keyboard():
    return ReplyKeyboardMarkup([["Шульте", "Алфавит", "Пирамида"],
                                ["Ещё!"]], resize_keyboard=True)

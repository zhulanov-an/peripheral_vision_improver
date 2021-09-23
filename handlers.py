from telegram import ReplyKeyboardMarkup

from utilites.create_shulte import create_all_tables
from utilites.utilites import get_emoji, get_keyboard


def greet_user(update, context):
    username = update.effective_user.first_name
    context.user_data['emoji'] = get_emoji(context.user_data)
    keyboard = ReplyKeyboardMarkup([["/shulte 3", "/shulte 5", "/shulte 7"]])
    text = f"Здравствуй, пользователь {username} {context.user_data['emoji']}! " \
           f"Это бот для тренировки периферийного зрения и памяти! Введите /shulte <num_cell> и получите " \
           f"таблицу Шульте! Доступны варианты на 3, 5, 7 ячеек"
    update.message.reply_text(text, reply_markup=get_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_emoji(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f"Здравствуй, {username} {context.user_data['emoji']}! Ты написал: {text}",
                              reply_markup=get_keyboard())


def send_shulte(update, context):
    cnt_cells = None
    path_to_pict = None
    chat_id = update.effective_chat.id
    create_all_tables()
    try:
        cnt_cells = int(context.args[0])
        if cnt_cells not in (3, 5, 7):
            raise ValueError
    except (ValueError, IndexError):
        update.message.reply_text("введите количество ячеек в формате /shulte <num>(доступно 3, 5, 7)",
                                  reply_markup=get_keyboard())

    if cnt_cells == 3:
        path_to_pict = "images/shulte_3_x_3.png"
    elif cnt_cells == 5:
        path_to_pict = "images/shulte_5_x_5.png"
    elif cnt_cells == 7:
        path_to_pict = "images/shulte_7_x_7.png"

    context.bot.send_photo(chat_id=chat_id, photo=open(path_to_pict, 'rb'))

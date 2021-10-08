from PIL import Image, ImageDraw, ImageFont
import random


def created_img(W:int, H:int):
    """Тут содаётся белый фон для пирамиды"""
    img = Image.new('RGBA', (W, H), 'white')
    return img


def sorted_words():
    """Тут мы отсеиваем подходящие слова из файла"""
    words = []
    with open('trainers/pyramid/word_rus.txt', 'r') as file:
        for line in file:
            if len(line.strip()) == 4:
                words.append(line.strip())
    return words
    

def format_word(number):
    """Из колекции слов выбираем случайные слова и форматируем их для пирамиды,
     делим по полам, вставляем пробелы, и по центру разделитель"""
    num = 2
    formated_text = []
    # Выбираем случайные слова пять штук
    words = random.sample(sorted_words(), number)
    for word in words:
        space = " " * num
        formated_text.append(f"{word[:2]}{space}*{space}{word[2:]}")
        num = num + 3
    return formated_text


def create_pyramid(number:int=5):
    """Строим из полученых слов пирамиду"""
    # Получаем размер изображения на котором будет строится пирамида
    W = 100 + 65 * number
    H = 22 * number + 40
    #Создаём новое изображение 
    img = created_img(W, H)
    # Чтобы пирамида была ровной используем свободный моноширный шрифт
    font = ImageFont.truetype('font/Fira_Code/static/FiraCode-Regular.ttf', 18)
    # Переменая для отсупов между словами по высоте
    space = 0
    text = format_word(number)
    for word in text:
        # Получаем размер слова
        w,h = font.getsize(word)
        #добавляем отступ
        space = space + 25
        idraw = ImageDraw.Draw(img)
        idraw.text(
            ((W-w)/2, space - (h/2) ),
            word,
            font=font,
            fill=('#000000'),
            )
    #Сохраняем получившуюся картинку
    return img.save('images/pyramid.png')

import os
import random

from PIL import Image, ImageDraw, ImageFont

from settings import FONT_PATH, IMAGE_DIR

ALPHABET = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")


def _draw_letters(d):
    h_points = list(range(100, 900, 30))
    w_points = list(range(100, 900, 30))
    random.shuffle(h_points)
    random.shuffle(w_points)
    random.shuffle(ALPHABET)

    for let, h_point, w_point in zip(ALPHABET, h_points, w_points):
        _draw_letter(
            d,
            size_font=random.randint(50, 100),
            letter=let,
            point=(h_point, w_point)
        )


def _draw_letter(d,
                 size_font,
                 letter,
                 point,
                 font=FONT_PATH,
                 color_font="black",
                 ):
    font = ImageFont.truetype(font, size_font)
    d.text(point, text=letter, fill=color_font, font=font)


def create_alphabet(size_by_side=1000, background="white"):
    img = Image.new('RGB', (size_by_side, size_by_side), color=background)
    d = ImageDraw.Draw(img)
    _draw_letters(d)
    img.save(os.path.join(IMAGE_DIR, 'alphabet.png'))


if __name__ == '__main__':
    create_alphabet()

import random

from PIL import Image, ImageDraw, ImageFont

_coordinate_lines_3_x_3 = [
    (0, 150, 450, 150),
    (0, 300, 450, 300),
    (150, 0, 150, 450),
    (300, 0, 300, 450)
]


def _get_odd_list(len_: int) -> list:
    cnt = 1
    result = list()
    while True:
        if cnt % 2:
            result.append(cnt)
        if len(result) == len_:
            return result
        cnt += 1


def _get_steps(num_by_side: int) -> list:
    return _get_odd_list(num_by_side)


def _get_line_coordinates(num_by_side: int) -> list:
    if num_by_side == 3:
        return _coordinate_lines_3_x_3
    else:
        raise RuntimeError(f'Количество ячеек {num_by_side} не поддерживается')


def _draw_cell(d, coordinate_lines, size_rectangle, color="black", width=5):
    d.rectangle((0, 0, size_rectangle, size_rectangle), outline=color, width=width)
    for coord in coordinate_lines:
        d.line(coord, fill=color, width=width)


def _draw_num(d, size_step: int, steps: list, size_font=50, font="arial.ttf", color_font="black"):
    font = ImageFont.truetype(font, size_font)
    points = list()
    for p_1 in steps:
        for p_2 in steps:
            points.append(((size_step * p_1) / 2, (size_step * p_2) / 2))

    nums = [str(i) for i in range(1, sum(steps) + 1)]
    random.shuffle(nums)

    for num, point in enumerate(points, start=1):
        d.text(point, text=nums.pop(), fill=color_font, font=font, anchor="mm")


def create_(num_by_side, size_by_side, background="white"):
    img = Image.new('RGB', (size_by_side, size_by_side), color=background)
    d = ImageDraw.Draw(img)
    coordinate_lines = _get_line_coordinates(num_by_side)
    _draw_cell(d, coordinate_lines, size_by_side)
    size_by_side_cell = size_by_side / num_by_side
    steps = _get_steps(num_by_side)
    _draw_num(d, size_by_side_cell, steps)
    img.save(f'images/cells_{num_by_side}_x_{num_by_side}.png')

import random

from PIL import Image, ImageDraw, ImageFont


def create_3_x_3():
    w, h = (450, 450)
    img = Image.new('RGB', (w, h), color="white")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 450, 450), outline="black", width=5)
    d.line((0, 150, 450, 150), fill="black", width=5)
    d.line((0, 300, 450, 300), fill="black", width=5)
    d.line((150, 0, 150, 450), fill="black", width=5)
    d.line((300, 0, 300, 450), fill="black", width=5)
    font = ImageFont.truetype("arial.ttf", 50)
    points = list()
    points.append((150 / 2, 150 / 2))
    points.append(((300 + 150) / 2, 150 / 2))
    points.append(((450 + 300) / 2, 150 / 2))
    points.append((150 / 2, (300 + 150) / 2))
    points.append(((300 + 150) / 2, (300 + 150) / 2))
    points.append(((450 + 300) / 2, (300 + 150) / 2))
    points.append((150 / 2, (300 + 450) / 2))
    points.append(((300 + 150) / 2, (300 + 450) / 2))
    points.append(((450 + 300) / 2, (300 + 450) / 2))

    nums = [str(i) for i in range(1, 10)]
    random.shuffle(nums)

    for num, point in enumerate(points, start=1):
        d.text(point, text=nums.pop(), fill="black", font=font, anchor="mm")

    img.save('simple_3_x_3.png')


if __name__ == '__main__':
    create_3_x_3()

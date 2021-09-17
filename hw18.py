# Написать скрипт, который будет создавать миниатюры фотографий.
# Объем полученого файла должен передаваться как параметр.


import os
from PIL import Image


def resize_image(resize_in_percent):

    img_obj = Image.open(os.getcwd() + '\\images\\img.jpg')
    percent = 100 / resize_in_percent
    width = int(float(img_obj.size[0])/percent)
    height = int(float(img_obj.size[1])/percent)

    resized_img = img_obj.resize(
        (width, height), Image.ANTIALIAS)
    resized_img.save(os.getcwd() + '\\images\\resized_img.jpg')


resize_image(20)
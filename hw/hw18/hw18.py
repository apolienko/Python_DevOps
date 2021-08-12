#!/bin/python
import sys
from PIL import Image

# Написать скрипт, который будет создавать миниатюры фотографий.
# Объем полученого файла должен передаваться как параметр.

if len(sys.argv) < 2:
    print("File name is not specified")
    exit(1)

picture = sys.argv[1]

def mini_pic(picture, width, length):
    with Image.open(picture) as img:
        a = [width, length]
        img.thumbnail(a)
        img.save("mini_" + picture)
        img.show()

mini_pic(picture, 50, 50)

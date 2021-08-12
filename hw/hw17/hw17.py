#!/bin/python
import os
import sys
from PIL import Image
from hw.hw16.hw16 import show_location

# Написать скрипт, который будет вытаскивать gps данные
# из фотографии (jpg файл) и передавать их на вход программе
# из hw16.txt

if len(sys.argv) < 2:
    print("File name is not specified")
    exit(1)

picture = sys.argv[1]

with Image.open(picture) as img:
    exif_data = img._getexif()
    latitude = exif_data[34853][2][0]   # 34853 -- GPS-tag (EXIF standard)
    longitude = exif_data[34853][4][0]

with open("gps1.txt", "w") as file:
    file.write("%d;%d" % (latitude, longitude))

show_location("gps1.txt")
os.remove("gps1.txt")



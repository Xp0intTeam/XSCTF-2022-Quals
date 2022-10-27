#!/usr/bin/env python3

import qrcode
from PIL import Image
from random import randint
from secret import flag

bias = 13
img = Image.open('./enc.png')
width, height = img.size

dec_img = Image.new(img.mode, (width//bias, height//bias), 1)

for w in range(width//bias):
    for h in range(height//bias):
        dec_img.putpixel((w, h), img.getpixel((bias*w+bias//2, bias*h+bias//2)))

dec_img.show()

#!/usr/bin/env python3

import qrcode
from PIL import Image
from random import randint
from secret import flag

bias = 13
img = qrcode.make(data=flag).get_image()
width, height = img.size

enc_img = Image.new(img.mode, (bias*width, bias*height), 1)

for w in range(width):
    for h in range(height):
        enc_img.putpixel((bias*w+bias//2, bias*h+bias//2), img.getpixel((w, h)))

with open('enc.png', 'wb') as f:
    enc_img.save(f)

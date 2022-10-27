from PIL import Image

img = Image.open('zelda-words.png')
W = img.size[0]
H = img.size[1]
img_res = Image.new("RGB", (W, H))
steg = "It seems like the words written on Sheikah Towers...?"
stegb = ''.join([bin(ord(x))[2:].rjust(8, '0') for x in steg])
if len(stegb) >= 3*W*H:
    print("[-] length WARNING!")

def set_lsb(x, c):
    c = ord(c) - ord('0')
    return ((x>>1)<<1) | c

pos = 0
flg = 1
for i in range(H):
    for j in range(W):
        pix = list(img.getpixel((j, i)))
        for k in range(3):
            if pos + k >= len(stegb):
                flg = 0
                break
            pix[k] = set_lsb(pix[k], stegb[pos+k])
        pos += 3
        img_res.putpixel((j, i), tuple(pix))

img_res.save('t.png')
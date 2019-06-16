from PIL import Image

im = Image.open("starmap.bmp", "r")
pix_val = list(im.getdata())
print(pix_val)
pix_val_flat = [x for sets in pix_val for x in sets]

flagchar = []

print(pix_val_flat)
for i in pix_val_flat:
    if i != 0:
        flagchar.append(chr(i))
flag = ""
print(flagchar)
for i in flagchar:
    flag += i
print(flag)
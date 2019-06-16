import base64

def base36decode(number):
    return int(number, 36)

data = ""
with open("OCR2.txt", "r") as f:
    data = f.read()

print("this is the data:\n", data)

data_fix = data.replace("O", "0")

print("fixed data:\n", data_fix)

decoded = base64.b16decode(data_fix)

with open("OCR3.txt", "w") as f:
    f.write(decoded.decode())

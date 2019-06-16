import base64

data = ""
with open("RmlsZW5hbWU.txt", "r") as f:
    data = f.read()

print(data)

data = data.split("\n")
thetext = []
print(data)
for i in data:
    if i != '':
        thetext.append(i)
print(thetext)
b64 = thetext[0]
b32 = thetext[1]
vinegar = thetext[2]

first_text = base64.b64decode(b64)
print(first_text.decode())

second_text = base64.b32decode(b32)
second_text = base64.b32decode(second_text)
second_text = base64.b32decode(second_text)
print(second_text.decode())

pass = 
count = 0
for i in vinegar:
    
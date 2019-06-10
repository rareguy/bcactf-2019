text = ""
viable = []
nth_char = []

with open("flag.txt", "rb") as f:
    data = f.read().decode()
    data = data.split('\n')
    nth_char = data[0].split(' ')
    print(nth_char, len(nth_char))
    for l in data:
        text = l
        if len(text) % 3 == 0 and text.find("&") == -1:
            print(text, len(text))
            viable.append(text)
x = len(viable)
print(x)

flag = ""
for i in range(len(nth_char)):
    flag += viable[i][int(nth_char[i])-1]
    print(flag)
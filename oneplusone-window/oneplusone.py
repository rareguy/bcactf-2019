data1 = ""
data2 = ""

with open("one.txt", "r") as f:
    data1 = f.read()

data1 = data1.split(" ")

print(data1)
with open("two.txt", "r") as f:
    data2 = f.read()

data2 = data2.split(" ")

print(data2)

alldata = []

for i in range(len(data1)):
    data1hex = int(data1[i], 0)
    data2hex = int(data2[i], 0)
    alldata.append(data1hex + data2hex)

print(alldata)
flag = ""
for i in alldata:
    flag = flag + chr(i)
    
print(flag)
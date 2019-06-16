import copy

letter_list = []
data = []


temp = " !\"#$%&\'()*+,-./"
temp_list = []
for i in temp:
    temp_list.append(i)
letter_list.append(temp_list)

temp = "0123456789"
temp_list = []
for i in temp:
    temp_list.append(i)
letter_list.append(temp_list)

temp = ":;<=>?@"
temp_list = []
for i in temp:
    temp_list.append(i)
letter_list.append(temp_list)


temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
temp_list = []
for i in temp:
    temp_list.append(i)
letter_list.append(temp_list)

temp = "[\]^_`"
temp_list = []
for i in temp:
    temp_list.append(i)
letter_list.append(temp_list)


temp = "abcdefghijklmnopqrstuvwxyz"
temp_list = []
for i in temp:
    temp_list.append(i)
letter_list.append(temp_list)

temp = "{|}~"
temp_list = []
for i in temp:
    temp_list.append(i)
letter_list.append(temp_list)

print(letter_list)

with open("inthtructhins.txt", "r") as f:
    temp = f.read()
    tempdata = temp.split(",")
    for i in tempdata:
        tmp = i.lstrip()
        tmp = tmp.strip("c")
        tmp = tmp.strip("r")
        data.append(tmp)

#print(data)

theflag = ""

for i in data:
    curletters = copy.deepcopy(letter_list)
    print(i)
    for reg in reversed(i):
        print(reg)
        if reg == "d":
            curletters.pop(0)
        elif reg == "a":
            curletters = curletters[0]
        #print(curletters)
    theflag = theflag + curletters

print(theflag)
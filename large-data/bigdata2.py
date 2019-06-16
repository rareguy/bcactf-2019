total_list = []
for i in range(27):
    total_list.append(0)
for k in range(100):
    temp_flag = ""
    for i in range(27):
        with open("OUT\\" + str(i) +"\\" + str(k), "r") as f:
            data = f.read()
            total = 0
            for j in data:
                total += ord(j)
            avg = total/len(data)
            cur = chr(int(avg))
            temp_flag += cur
            total_list[i] += ord(cur)
    print(temp_flag)
    print(total_list)
flag = ""
for i in total_list:
    print(chr(int(i/100)))
    flag += chr(int(i/100))

print(flag)
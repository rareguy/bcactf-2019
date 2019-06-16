# Items:
# 
# A: $45, no sale
# B: $52, buy one get one 10% off
# C: $67, buy one get one half off
# D: $75, buy two get one free

# Test case:
# In
# C B B C A 250
# D A B B 250
# D D D D D A B 390
# 
# out
# 5.70
# 31.20
# -1



data = ""
with open("input.txt", "r") as f:
    data = f.read()

print(data)

data = data.split("\n")
print(data)

answer = []

for i in data:
    grand_total = 0.00
    change = 0.00
    element = i.split(" ")
    print(element)
    b_flag = 0
    c_flag = 0
    d_flag = 0
    for letter in element:
        if letter == "A":
            print("BOUGHT A")
            grand_total = grand_total + 45.00
        elif letter == "B":
            if b_flag == 0:
                print("BOUGHT B")
                grand_total = grand_total + 52.00
                b_flag = 1
            elif b_flag == 1:
                print("10% OFF B")
                grand_total = grand_total + 52 - 52/10
                b_flag = 0
        elif letter == "C":
            if c_flag == 0:
                print("BOUGHT C")
                grand_total = grand_total + 67.00
                c_flag = 1
            elif c_flag == 1:
                print("HALF PRICED C")
                grand_total = grand_total + 67/2
                c_flag = 0
        elif letter == "D":
            if d_flag != 2:
                print("BOUGHT D")
                grand_total = grand_total + 75.00
                d_flag = d_flag + 1
            elif d_flag == 2:
                print("FREE D")
                d_flag = 0
        else:
            cash = float(letter)
            change = cash - grand_total
        print("Current total:", round(grand_total, 2))
    print("The total is ", round(grand_total, 2))
    print("The change is ", round(change, 2))
    if change >= 0:
        answer.append(round(change, 2))
    else:
        answer.append(-1)

for i in answer:
    print(i)
    

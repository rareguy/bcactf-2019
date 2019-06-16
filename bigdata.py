# import os
#  
# path = 'OUT'
#  
# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in f:
#         files.append(os.path.join(r, file))
#  
# hugestrings = ""
#  
# for f in files:
#     with open(f, "r") as f:
# #         print(f.read())
#         hugestrings = hugestrings + f.read()
#  
# with open("result", "w") as f:
#     f.write(hugestrings)


# for i in range(27):
#     curstr = ""
#     for j in range(100):
#         with open("OUT\\" + str(i) + "\\" + str(j), "r") as f:
#             curstr += f.read()
#     with open("eachfolder\\" + str(i), "a") as f:
#         f.write(curstr)
import string
import operator
import base64 

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches
 
# print(list(find_all('spam spam spam spam', 'spam'))) # [0, 5, 10, 15]
 
 
def common_elements(list1, list2):
    return list(set(list1) & set(list2))
 
occurences = []
occurence = []
data = ""
theflag =""
for i in range(27):
    print(i)
    with open("eachfolder\\" + str(i), "r") as f:
        data = f.read()
        occurence_temp = {}
        total = 0
        for i in data:
            total += ord(i)
        avg = total/len(data)
        ch = int(avg)
        print(ch)
        theflag += chr(ch)
#         for j in string.ascii_letters + "0123456789_!@#$%^&*()?~+[]{}\\|;\'\",.<>/`:":
#             occurence_temp[j] = data.count(j)
#         occurence.append(occurence_temp)
#         occurences_temp = []
#         temp2 = {}
#         for i in string.ascii_letters + "0123456789_!@#$%^&*()?~+[]{}\\|;\'\",.<>/`:":
#             occurences_temp = list(find_all(data, i))
#             temp2[i] = occurences_temp
#         occurences.append(temp2)
print(theflag)
flagstart = "bcactf{"
for i in range(len(theflag)):
    try:
        print(ord(theflag[i]) - ord(flagstart[i]))
    except:
        if range == 26:
            print(ord(theflag[i]) - ord("}"))
        else:
            continue
    

# print(occurences)

# flagstart = "bcactf{"
# for i in range(len(flagstart)):
#     print(flagstart[i], occurences[i][flagstart[i]])
# 
# print("}", occurences[26]["}"])


# # print(occurences)
# print(occurence)
# for i in occurence:
#     lettertotalmax = max(i.items(), key=operator.itemgetter(1))[0]
#     lettertotalmin = min(i.items(), key=operator.itemgetter(1))[0]
#     print(lettertotalmax, lettertotalmin)



# first_occurences = common_elements(occurences[0], occurences[1])
# print("first occurences:", first_occurences)
# second_occurences = common_elements(first_occurences, occurences[2])
# print("second occurences:", second_occurences)
# third_occurences = common_elements(second_occurences, occurences[3])
# print("third occurences:", third_occurences)
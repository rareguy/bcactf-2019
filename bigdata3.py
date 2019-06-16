# list_of_data = []
# 
# for i in range(100):
#     curstr = ""
#     for j in range(27):
#         with open("OUT\\" + str(j) + "\\" + str(i), "r") as f:
#             curstr += f.read()
#     
#     #print(curstr)
#     list_of_data.append(curstr)
#     with open("splittofilenum\\" + str(i), "w") as f:
#         f.write(curstr)

import string
import matplotlib.pyplot as plt

occurence = []
for i in range(100):
    print(i)
    with open("splittofilenum\\" + str(i), "r") as f:
        data = f.read()
        occurence_temp = {}
        for j in string.ascii_letters + "0123456789_!@#$%^&*()?~+[]{}\\|;\'\",.<>/`:":
            occurence_temp[j] = data.count(j)
        occurence.append(occurence_temp)

for i in range(len(occurence)):
    print(i)
    print(occurence[i])
    
# for i in range(len(occurence)):
#     plt.bar(range(len(occurence[i])), list(occurence[i].values()), align='center')
#     plt.xticks(range(len(occurence[i])), list(occurence[i].keys()))
# # # for python 2.x:
# # plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# # plt.xticks(range(len(D)), D.keys())  # in python 2.x
# 
# plt.show()
# flagstart = "bcactf{"
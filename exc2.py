bf = ""
with open("exc2.txt", "r") as f:
    bf = f.read()

brain = bf.split("\n")
print(brain)
brainfuck = ""
for i in brain:
    brainfuck += i
print(brainfuck)
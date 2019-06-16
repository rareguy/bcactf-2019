rune = ""
with open("runewords.txt", "r") as f:
    rune = f.read()

import string

def find_position(char):
    for set_num in range(len(table)):
        if char in table[set_num]:
            return set_num
    return False

def forge_offsets(key, direction, offset):
    if type(key) is str:
        return [(string.ascii_uppercase.index(x) + offset) * direction for x in key]
    else:
        return [(x + offset) * direction for x in key]

def frequency(text):
    return {letter: text.count(letter) for letter in string.ascii_uppercase}

######
#
#  Scroll down for the bits you should interact with
#
######

table = [
  ["ᚠ", "F"], 
  ["ᚢ", "V"],
  ["ᚦ", "TH"],
  ["ᚩ", "O"],
  ["ᚱ", "R"],
  ["ᚳ", "C"],
  ["ᚷ", "G"],
  ["ᚹ", "W"],
  ["ᚻ", "H"],
  ["ᚾ", "N"],
  ["ᛁ", "I"],
  ["ᛂ", "J"],
  ["ᛇ", "EO"],
  ["ᛈ", "P"],
  ["ᛉ", "X"],
  ["ᛋ", "S"],
  ["ᛏ", "T"],
  ["ᛒ", "B"],
  ["ᛖ", "E"],
  ["ᛗ", "M"],
  ["ᛚ", "L"],
  ["ᛝ", "ING"],
  ["ᛟ", "OE"],
  ["ᛞ", "D"],
  ["ᚪ", "A"],
  ["ᚫ", "AE"],
  ["ᚣ", "Y"],
  ["ᛡ", "IA"],
  ["ᛠ", "EA"]
]

for i in rune:
    for j in table:
        if i == j[0]:
            rune.replace(i, j[1])
            break

print(rune)
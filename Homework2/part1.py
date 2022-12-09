# 1. Write a function which will return how many times a word (symbols separated with space, coma and dot) meet in the string
# Input: s – string
# Output: word1 = number, word2 = number
# Input: s= “Tom eats and eats”
# Output: Tom = 1, eats = 2, and = 1

import re

s = "Tom eats.and,eats"
a = re.split(' |,|\.', s)
d = {}

for word in a:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)

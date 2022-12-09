# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.
# 2. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
#
# 3. Count number of vowels (a,o,u,e,i) in the string s
# Intput: s – string
# Output: Number of vowels = XX

import re

text = input("Enter some text and I will count the vowels: ")

pattern = re.compile("[aeiou]", re.IGNORECASE)
result = [i for i in text if pattern.match(i)]

print(len(result))

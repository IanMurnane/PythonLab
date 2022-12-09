# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.
# 2. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
#
# 3. Count number of vowels (a,o,u,e,i) in the string s
# Intput: s – string
# Output: Number of vowels = XX

from math import pi

radius = float(input("Enter the radius of a circle: "))
area = pi * radius * radius
print("The area of the given circle is: ", area)

#  4. Write a Python program to convert a given list of strings into list of lists using map function

l = ['one', 'two', 'three', 'four']

ll = list(map(lambda s: [s], l))

print(ll)

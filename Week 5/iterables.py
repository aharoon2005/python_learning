# Iterables = An object / collection that can return its elements one at a time,
#                         allowing it to be itterated over in a loop

list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)

for item in list:
    print(item, end=' ' )

for item in reversed(list):
    print(item, end=' ')

for item in tuple:
    print(item, end=' ')

# Sets work differently than lists and tuples.

fruits = {'apple', 'banana', 'orange', 'coconut'}

for fruit in fruits:
    print(fruits)

#for fruit in fruits:           # Sets are not reversible
#    print(reversed(fruits))

name = "Aydin Haroon"

for character in name:
    print(character, end='')

# Dictionaries can be iterated but will only return the keys and not the value

dict = {"A": 1, "B": 2, "C": 3}

for key in dict:
    print(key)

for value in dict.values():   # using .value() will return the values but not the keys
    print(value)

for key, value in dict.items():
    print(f'{key} = {value}')
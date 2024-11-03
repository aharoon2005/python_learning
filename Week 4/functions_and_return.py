# a function is a block of reusable code
#                           Place () after the function name to invoke it

def happy_birthday():
    print('Happy birthday to you')
    print('you live in a zoo')
    print('you look like a monkey')
    print('and you smell like one too')
    print()

happy_birthday()

def happy_birthday_2(name):
    print(f'Happy birthday to {name}')          # Note the "f" before the string literal. This allows me to embed an expression inside a string
    print('you live in a zoo')
    print('you look like a monkey')
    print('and you smell like one too')
    print()

happy_birthday_2('Aydin')


def happy_birthday_2(name, animal):            # name and animal are just placeholders
    print(f'Happy birthday to {name}') 
    print('you live in a zoo')
    print(f'you look like a {animal}')
    print('and you smell like one too')
    print()

happy_birthday_2('Aydin', 'lizard')

# Return is a statement used to end a function
#                       and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name('Aydin', 'Haroon')

print(full_name)

#from factorial import calculate_factorial  # You can import multiple functions from different folders

#print(calculate_factorial(4))


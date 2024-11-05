#  positional arguments are arguments
#  that are passed to a function based on 
#  their position or order in the function call


def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")    

hello('hello','Mr.','Aydin','Haroon')


#  Default arguments are arguments where a default value for certain parameters
#  Default is used when that argument is omitted
#  Makes your functions more flexible, reduces # of arguments


def net_price(list_price, discount = 0, sales_tax = 0.05):
    return list_price * (1 - discount) * (1 + sales_tax)

print(net_price(500)) #instead of needing values for discount and sales tax which always stays the same, set discount & sales tax == to a number


# Keyword arguments are arguments preceded by identifiers
# Helps with readibility
# order of arguments do not matter


def Hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")    

Hello('hello', last='Haroon', first='Aydin', title='Mr.' ) # Keyword arguments can be placed anywhere in the function call except for before the initial string 
                                                           # Positional arguments MUST come first


# Arbitrary Arguments
# "*args" = allows you to pass multiple non-keyword arguments
# "**kwargs" = allows you to pass multiple keyword arguments
#   "*" = unpacking operator


def add(*args):   # will turn any argument you put in into a tuple
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))   # can pass in any number of args and it will add them all up

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Aydin", "Haroon", "Moiz", "Haroon", "Mindy", "Haroon")

# **kwargs =

def print_adress(**kwargs):         
    for key, value in kwargs.items():     #**kwargs turns any argument given into a dictionary with a key and a value.
        print(f"{key}: {value}")


print_adress(street='123 Fake street',
             apt= '100',
             city="detroit" ,
             state='MI' ,
             zip= "54321" )

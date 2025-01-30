Integers=[1,2,3,4,5]     # A for loop is a programming construct that repeatedly executes a block of code until a condition is met
for number in Integers:
    print(number)

for number in Integers:
    print('meow')

for number in Integers:
    print(number + number)

dict_Aydin = {'name':'Aydin Haroon', 'weight':'170 lbs', 'favorite foods':['sushi','salmon','udon']}

for me in dict_Aydin.values():
    print(me)
    
for key, Value in dict_Aydin.items():
    print(key, '->', Value)

Flavors = ['Cookie Dough', 'Oreo', 'Rocky Road']                    # a nested for loop is a loop that is placed inside another loop. 
Toppings = ['Hot Fudge', 'Sprinkles', 'Chocolate Chips']            # The outer loop iterates over a sequence of items,
for one in Flavors:                                                 # and for each item in the outer loop, the inner loop iterates over another sequence of items.
    for two in Toppings:
        print(one, 'topped with', two)



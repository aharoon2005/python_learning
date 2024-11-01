number_1 = 0

while number_1 < 5:
    print(number_1,)                #A while loop is a control flow statement that repeats a set of instructions until a condition is met
    number_1= number_1 + 1

number_2 = 0

while number_2 < 5:
    print(number_2)
    if number_2 == 3:               # break statment will break the loop if the if statment becomes true
        break 
    number_2 = number_2 + 1

number_3 = 0

while number_3 < 5:
    print(number_3)
    if number_3 == 6:               # Adding an else statement will only work if the if statment never happens
        break
    number_3 = number_3 + 1
else:
    print('No longer < 5')

number_4 = 0

while number_4 < 5:
    print(number_4)
    if number_4 == 3:           # This will create an infinite loop which will never stop running, hence the continue being in quotes.
        'continue'         
    number_4 = number_4 + 1



if 25>10:
    print('Correct!')   # if statments controls the flow of a program by executing different code blocks based on whether a condition is true or false

if 25<10:
    print('Correct!')
else:
    print('Wrong!')     #specifies that alternate processing is to take place when the conditions of the matching IF statement are not satisfied


if 25<10:
    print('Correct!')
elif 25<30:
    print('Correct!')   # elif runs after if statement if the if statment is false. You can have as many elif statments as you want, but the first elif statment to be true will give your output.
else:                       
    print('Wrong!')  

if(20<10) or (1<3):
    print('Correct!')
    if 25>10:
        print('nested if is correct!')  #a nested if statement is an if statement that is placed inside another if statement. This allows you to check for multiple conditions in a hierarchical manner.
    print('Correct!')
else:
    print('Wrong!') 


def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Define the number directly
number = -10  # You can change -10 to any other number
result = check_number(number)
print(result)

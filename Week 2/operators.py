'=='    # Equal to
'!='    # Not equal to
'>'     # Greater than
'<'     # Less than
'>='    # Greater than or equal to
'<='    # Less than or equal to 

'and'   # Returns "True" if both statement are true
'or'    # Returns "True" if one of the statments is true
'not'   # Reverses the result, returns false if the statement is true and vice-versa

print(10==10) # This will output "True"
print(10==50) # This will output "False"  

print(10!=10) # This will output "False"
print(10!=50) # This will output "True"

print(10>50)  # Because 10 is less than 50, this will output "False"
print(50>10)  # Because 50 is greater than 10, this will output "True"

print(10<50)  # Because 10 is less than 50, this will output "True"
print(50<10)  # Because 50 is greater than 10, this will output "False"

print(10>=50)  # Because 10 is less than 50 and not equal to 50, this will output "False"
print(10>=10)  # Because 10 is equal to 10, this will output "True"
print(50>=10)  # Because 50 is greater than 10 but not equal to 10, this will still output "True"

print(10<=50)  # Because 10 is less than 50 and not equal to 50, this will output "True"
print(10<=10)  # Because 10 is equal to 10, this will output "True"
print(50<=10)  # Because 50 is greater than 10 but not equal to 10, this will still output "False"

print(
    (50>10) or (50<10)     # if one of these statments is correct, it will output "True"
)

print(
    (50<10) or (50==10)     # if both of these statments are false, it will output "False"
)

print(
    (50>10) and (50<10)     # if one of these statments is correct, it will output "False" because both are not correct
)

print(
    (50>10) and (10<=10)     # if one of these statments is correct, it will output "True" because both are correct
)

print(
    not(50==50)              # "not" will tell you the opposite of the correct outcome so this will output "False" even though 50 does equal 50
)


x=int(1+2)          #Integers are whole numbers
print(x)

y=int(1+2.5)        #Will not add decimal numbers (just prints 1+2=3)
print(y)

z=float(1+2.5)      #Float allows you to work with decimal numbers
print(z)

f=complex(3j)       #complex numbers (self explanatory, most likely will never be used)
print(f)

g=bool(1==5)        #Boolean acts as a true or false. 
print(g)

'Hello World!'       #Use single quotes when there are no apostrophes in your sentence
"I've fallen"       #Use double quotes when there ARE apostrophes in your sentence

multiline="""       
My name is Aydin
I have brown hair
"""
print(multiline)    #use triple quotes when you have multiple lines of text (''' or """)

h='Hello World!'    #Strings can be indexed meaning you can search withing it and it starts at 0 [:5] = [0:5]
print(h[:5])        #[:5] will print the first 5 charcters in the string
print(h[6])         #[6] will print only the 6th character in the string
print(h[-3])        #[-3] will print the 3rd character starting from the right side of the string
print(h[:-3])       #[:-3] will pring the whole string except for the last 3 characters
print(h*3)          # You can multiply strings

list=[1,2,3]        #lists hold multiple seperate values 
print(list)
print(list[0])      #[0] will print the first value in the list

list.append(4)      #adding .append will add a value to the end of a list
print(list)

list_strings=['hi','hello','hola']
print(list_strings)
print(list_strings[1])     # You can list strings as well

list_strings[0]='goodbye'  # You can change the values of a list using this 
print(list_strings)

nested_list=['hi',3,['sad','happy'],True]   # You can add different data types to a list
print(nested_list[2])                       # This will print the 3rd value in the list
print(nested_list[2][0])                    # This will print the 1st value in the list which is the 3rd value of the main list

tuple=(1,2,3,2,1)   #tuples are used for data sets that will never change such as city names or universal constants
print(tuple[2])
# tuple.append(3)=error     # You cannot change tuple lists

set={1,2,3}         # Sets cannot be indexed and are unordered meaning you cannot print(set[1])
set2={1,1,2,20,3,3,31,4,20}
print(set2)         # Will only pring the unique values from least to greatest
set3={1,1,5,32,33,4,3,21}
print(set3 | set2)  # "|" will compare two sets
list1 = [1,2,3,4,5]
statement = "I'm a student"
tuple1 = (11,12,13,14,15)

#The in operand is used to check whether or not an element can be found in a variable or list

print(3 in list1) #True because 3 is found in the list
print("a" in statement) #True because the word "a" is on the statement variable
print(17 in tuple1) #False cause 17 was not found in tuple1

the_list = [2,4,6,8]
string = "Coding is getting tedious"
tuple = (5,10,15,20)

#The not in operand is used to see what is not in a list or string

print(8 not in the_list) #False because 8 is included in the variable the_list
print("Coding" not in string) #False because "Coding" is included in string
print(25 not in tuple) #True cause 25 isn't in the tuple

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1) #False since 5 and 5 are equal 
print(x2 is y2) #True since both string variables are equal
print(x3 is y3) #False since both lists are viewed as separate by python interpreter

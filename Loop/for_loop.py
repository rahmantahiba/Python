#For loops

#syntax for range: (stop, step, size)

str = "Python"; 

#str is the variable 

def starter():
    for i in str:
        print(i); 

#Do multiplication for the given list

def multiple():
    list = [1,2,3,4,5,6,7,8,9,10] 
    user = int(input("Enter the number to perform multipcation: "))
    for m in list:
        operation = user * m
        print(operation)

#Print the sum of the list

def sum():
    add_list = [10,20,30,40]
    sum = 0 #intilizing to take in int value
    for a in add_list:
        sum = sum + a 
    print("The sum of the value is", sum) #Needs to be outside of the loop or else it will print the list

def basic_range():
    for r in range(10): #to print out 1 to 10
        print(r, " "); 

#Do multiplication using for in range

def multiply():
    user_input = int(input("Enter a number to perform multiplication: "))
    for multi in range(1, 12): #1 is the starting position but the default is 0
        operate = user_input * multi
        print(user_input, "*", multi, "=", operate)

#The len function helps with iterating through indexes 

def list_name():
    name_list = ["Peter", "Joseph", "Ricky"]
    for n in range(len(name_list)):
        print(name_list[n]); 

def index():
    num = [1,2,3,4]
    for number in range(len(num)):
        value = num[number]
        print(number, value) #How to access indexes 

#Nested for loop example

def nested():
    rows = int(input("Enter the rows: "))
    for p in range(0, rows+1):
    #to print the numbers of rows and adding 1 for the asterisk
        for j in range(p):
            print("*", "\n")

def main():
    starter()
    multiple()
    sum()
    basic_range()
    multiply()
    list_name()
    index()
    nested()

main()

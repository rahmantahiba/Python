"""
If statement is to see whether or not the condition is true 
and if it isn't the code won't execute 

"""

def if_statement():

    even = 2
    if even % 2 == 0: 
        print("The number is even")

"""

The if-else statement is used to test a condition and the else 
condition also checks that it can be either true and false to ensure
that the code will run even with false statement. 

"""

def else_statement():

    num = int(input("Put a number: "))
    if num % 2 == 1:
        print("Number is odd")
    else: 
        print("Number is even")

"""

Who is the oldest? Use conditions to figure out. 

"""

def age():

    first_age = int(input("Enter first sibling age: "))
    second_age = int(input("Enter second sibling age: "))
    third_age =  int(input("Enter third sibling age: "))

    if first_age > second_age:
        print("The oldest sibling is first sibling")
    elif second_age > third_age:
        print("The oldest sibling is the second sibling")
    elif third_age > second_age: 
        print("The third sibling is the oldest siblings")
    else:
        print("None")

"""

Create a conditional regarding grades 

"""

def grades():

    marks = int(input("Enter your grade: "))
    if marks > 90 and marks <= 100:
        print("A")
    elif marks >= 75 and marks >= 85:
        print("B")
    elif marks >= 60 and marks >= 70:
        print("C")
    elif marks <= 59 and marks == 50:
        print("D")
    else:
        print("F")

def main(): 
    if_statement()
    else_statement()
    age()
    grades()

main()

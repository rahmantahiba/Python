#Printing 1 through 10 using while loop 

from re import S


def one_ten():
    i = 0
    while i <= 10:
        print(i) #Don't forget to increment
        i += 1

#Print out multiplication table using while loop

def multiple():
    start = 1
    user = int(input("Enter the number to perform multiplication: "))
    while start <= 12:
        operate = user * start
        print(start, "*", user, "=", operate)
        start += 1

#Review 

def square():
    initial = 0
    while initial <= 10:
        s = initial**2
        initial += 1
        print("The exponent by 2 is:", s)

def input_square():
    initial = 0
    i = int(input("Enter the number for the exponent: "))
    while initial <= 10:
        solve = initial**i
        initial += 1 #Do not increment solve
        print(initial,"^", i,"=", solve)

def odd_even():
    s = 0
    while s <= 10:
        if(s % 2 == 1):
            print(s, "Odd")
        else:
            print(s, "Even")
        s += 1

def main():
    one_ten()
    multiple()
    square()
    input_square()
    odd_even()

main()
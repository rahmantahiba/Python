#Printing 1 through 10 using while loop 

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

def main():
    one_ten()
    multiple()

main()
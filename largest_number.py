def large_num():

    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    third = int(input("Enter the third number: "))
    if first > second and first > third:
        print("The greatest number is: ", first)
    elif second > first and second > third:
        print("The greatest number is: ", second)
    elif third > first and third > second:
        print("The greatest number is: ", third)
    else: 
        print("All the same")

def main(): 
    large_num()

main()
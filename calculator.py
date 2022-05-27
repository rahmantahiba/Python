def calculate():

    sign = (input("Enter the operator: "))  #Doesn't need char 
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))

    if sign == '+':
        print(num_1 + num_2)
    elif sign == '-':
        print(num_1 - num_2)
    elif sign == '*':
        print(num_1 * num_2)
    elif sign == '/':
        print(num_1 / num_2)
    else: 
        print("Please enter the right number")

def main():
    calculate()
    

main()
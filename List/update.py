#Updating list in multiple ways 

def change_list():

    num = [1,2,3,4]
    print("The original list: ", num)

    num[2] = 10
    print("Adding 10 to the second index: ", num)

    num[1:2] = [80,81]
    print("Adding multiple elements: ", num)

    num[-1] = 5
    print("Adding an element to the end of the list: ", num)

#Repeating elements in a list 

def repetition():

    r_list = [2,4,6,8]
    print(r_list * 2)

#Concatenating a list means two lists get combined by using +

def concatenate():

    f = [1,2,3]
    s = [4,5,6]
    print(f + s)

def main():
    change_list()
    repetition()
    concatenate()

main()
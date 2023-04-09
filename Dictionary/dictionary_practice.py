def concatenate_dict():
    dict1 = {1:10, 2:20}
    print(dict1)
    dict1.update({3:30, 4:40, 5:50, 6:60}) #use update to add additional keys and values to the dictionary 
    print(dict1)

def key_in_dict():
    x = int(input("Enter a number key of dictionary: "))
    dict = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
    if x in dict:
        print("Key is present in dictionary")
    else:
        print("Key not present in dictionary")

def dict_contain(x):
    dict_multiple = {x: x * x for x in range(1,x)}
    print(dict_multiple)

def main():
    concatenate_dict()
    key_in_dict()
    dict_contain(6)

main()
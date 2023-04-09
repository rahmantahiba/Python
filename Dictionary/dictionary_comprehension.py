#Using dict method 

def dict_method():
    square_dict = dict()
    for num in range(1,11):
        square_dict[num] = num * num #storing the num for dictionary list
    print(square_dict)

def dict_comprehension():
    square_dict = {num : num * num for num in range(1,11)}
    print(square_dict)

def condition_dict_comprehension():
    dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
    dict_even = {key : v for (key, v) in dict.items() if v % 2 == 0}
    dict_odd = {key : v for (key, v) in dict.items() if v % 2 == 1}
    print("Even:", dict_even, "Odd:", dict_odd)

def main():
    dict_method()
    condition_dict_comprehension()

main()
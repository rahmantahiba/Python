#Regular for loop

def for_loop_method():
    h_letter = [] #to print the letters as a list 
    for letter in 'human':
        h_letter.append(letter) #append adds each letter to the []

    return h_letter

#List comprehension method

def list_comprehension_method():
    h_letters = [letter for letter in 'human'] #[expression loop]
    return h_letters


def comprehension_conditionals():
    even_odd = ["Even" if n % 2 == 0 else "Odd" for n in range(10)]
    return even_odd


def main():
    print(for_loop_method())
    print(list_comprehension_method())
    print(comprehension_conditionals())

main()

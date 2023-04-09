def for_divisible_seven():
   num = []
   for i in range(1,1000):
        if i % 7 == 0:
            num.append(i)
        print(num)

def divisible_seven():
    div_seven = [num for num in range(1,1000) if num % 7 == 0]
    return div_seven

def multiplication_table(rows, col):
    multiple = [[i * j for i in range(rows + 1)] for j in range(col + 1)]
    return multiple

def multiple_table(num):
    multiply = [m * num for m in range(0,10)]
    return multiply

def main():
    for_divisible_seven()
    print(divisible_seven())
    print(multiplication_table(5,5))
    print(multiple_table(5))

main()
#My way make sure the return statement is outside the while loop

def insertion_sort(array):
    for i in range(1,len(array)):
        value_to_sort = array[i] #iterating through list
        while array[i-1] > value_to_sort and i > 0: #the i > 0 is to ensure it doesn't go to negative index
            array[i], array[i-1] = array[i-1], array[i] #the switch 
            i -= 1 #to keep looking through the left index
    return array

#Another way

def insertion_sort_again(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    array = [8,2,6,4,5]
    print(insertion_sort(array))
    arr = [8,2,6,4,5]
    print(insertion_sort_again(arr))

main()
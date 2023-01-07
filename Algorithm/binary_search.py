""""

Note-Taking: Iterative method for binary search

"""

"""Establishing the binary search formula to find the mid element"""

def binarySearch(array,k,low,high):
    while low <= high:
        middle = low + (high - low)//2
        if array[middle] == k:
            return middle

        elif array[middle] < k:
            low = middle + 1

        else:
            high = middle - 1

    return -1

"""Code is executed"""

array = [1,3,5,7,9] #Making the array
k = 5 #The element that needs to be found 
result = binarySearch(array,k,0,len(array)-1)

"""

1) The result variable is calling the function to find the formula

2) The 0 is the lowest element 

3) The -1 is to ensure the array backtracks to find the middle element 

4) The length functions calculates the size of the array to ensure there is no error in array size.

"""

if result != -1:
    print("Element is present at index:" + str(result)) #For int to be turned to a string

else:
    print("Element not found")

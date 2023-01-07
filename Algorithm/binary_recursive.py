""""

Note-Taking: Recursive method for binary search

"""

"""Establishing the binary search formula to find the mid element"""

def binarySearch(array,k,low,high):
    if high >= low:
        middle = low + (high - low)//2

        if array[middle] == k:
            return middle
        
        elif array[middle] > k:
            return binarySearch(array,k,low,middle-1) #calling function to check the condition for middle-1

        else: 
            return binarySearch(array,k,middle+1,high) #calling function to check the condition for middle+1

    else:
        return -1

array = [1,3,4,7,9]
k = 7

result = binarySearch(array,k,0,len(array)-1)

if result != -1:
    print("Element is present at index: " + str(result))

else:
    print("Element not found")
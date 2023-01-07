def LinearSearch(a,n,num):
    for i in range(0,n):
        if(a[i] == num):
            return i

    return -1 #-1 to keep track of the array

a = [1,2,3,5,6,7]
num = 5
n = len(a) #Takes in the length of the array 

result = LinearSearch(a,n,num) #Calling the function so the function can perform within a variable

"""

Iterating through the list and function to ensure that the index is found through 
linear search 

"""

if(result == -1):
    print("Element is not found")

else:
    print("Element found at index:", result)

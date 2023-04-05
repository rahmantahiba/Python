"Divide and conqouring separating and copying the array"

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left) #recursive call for left and right
        merge_sort(right)

        i = 0 #two halves iteration 
        j = 0

        k = 0 #main list

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i] #iterating through the left side 

                i += 1

            else:
                arr[k] = right[j] #iterating through right side
                j += 1
            k += 1 #move to the next slot

        #for the remaining values 
        while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

        while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

def main():
  unsorted = [54,26,93,17,77,31,44,55,20]
  arr = [54,26,93,17,77,31,44,55,20]
  merge_sort(arr)
  print("Unsorted array:", unsorted)
  print("Sorted array:", arr)

main()
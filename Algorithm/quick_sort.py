def quick_sort(sequence):
    length = len(sequence)
    if length <= 1: #goes over values that are less than or equal to one and returns the sequence
        return sequence
    else:
        pivot = sequence.pop() #removes the last element and also returns it

    #move through the sequence or items (empty list)

    more_items = []
    less_items = []

    for item in sequence:
        if item > pivot:
            more_items.append(item)
        else:
            less_items.append(item)

    return quick_sort(less_items) + [pivot] + quick_sort(more_items) #recursive call

def main():
    unsorted_sequence = [5,6,7,8,9,8,7,6,5,6,7,8,9,0]
    sequence = [5,6,7,8,9,8,7,6,5,6,7,8,9,0]
    print("Unsorted array:", unsorted_sequence)
    print("Sorted array:", quick_sort(sequence))

main()
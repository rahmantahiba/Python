#Lists are mutable which means that the element can be changed when accessed from index

"""Lists are ordered and if it isn't it will return false"""

#True 

def true():
    a = ["HELLO", "THERE"]
    b =  ["HELLO", "THERE"]

    if(a == b):
        print("True")
    else:
        print("False")

#False 

def false():
    first = [1,2,3]
    second = [1,2,3,4]

    if(first == second):
        print("True")
    else:
        print("False")

"""

A list has (start,stop,step)

Start: The starting index position 

Stop: The last index of the list

Step: Skips the nth element that's why the indexes are counted by 0,1,2,3... -1 

"""

#A colon is used for slicing 

def slice():
    the_list = ["My", "name", "is", 1] #Only "my" is printed cause everything after 1 is sliced
    print(the_list[0:1])

def take_length():

    l = [1,2,3,4]
    print(len(l))

def main():
    true()
    false()
    slice()
    take_length()

main()

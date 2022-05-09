#Printing "Hello World"

x = "Hello World"
print(x)

#Multiple Assignment 

a,b,c = 1,2,"Est"
print(a,b,c)

#Using del

list1 = [1,2,3,4]
list2 = ["Hello", "There"]
del list2[1]
print(list1, list2)

#Types of string
#The [] and [:] is called the slice operator that helps pic a specific index

str = "Hello World"
print(str)
print(str[0])
print(str[2:6])
print(str[2:])
print(str * 2) #Print str two times
print(str + " TEST") #Concatenated string "Hello World Test" to add a new string

#Lists 
#Index is called element 

name = ["Athanasia", "Jeanette", "Luca"]
age = [10,10,9]

print(name[0])
print(name[1:])
print(age * 2)
print(name + age) #Combine the two lists

#Tuples use () 

job = ("Student", "Teacher", "Doctor", "Lawyer")
fav = (0, 4, 2, 3)

print(job[1:])
print(job[0:3])
print(fav * 2)
print(job + fav) #Combine the two tuples

#Type conversion 

#List is converted to tuple

s = [1,2,3,4]
print(tuple(s))








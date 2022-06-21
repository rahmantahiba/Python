#Attempt at reading "Simple.txt"

with open('File Reading/Simple.txt', 'r') as read:
    content = read.read()
    print(content)

#The readline command is entered two time so both of the strings can get printed

with open('File Reading/Simple.txt') as s:
    c = s.readline()
    print(c, end='')

    c = s.readline()
    print(c, end='') #End is for whitespace and not new line

with open('File Reading/List.txt', 'r') as f:
        for line in f:
            print(line, end='') #Iterating through the file to save memory and make the code efficient

#More control for file reading by using "read" command

with open('File Reading/List.txt') as a:
    con = a.read(100)
    print(con, end='')


#Using a while loop to read a file

with open('File Reading/List.txt', 'r') as c:
    size = 100
    contents = c.read(size)

    while len(contents) > 0:
        print(contents, end='')
        contents = c.read(size) 

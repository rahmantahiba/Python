class Dog:

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    
    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def display(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Color:", self.__color)

def main():

    D = Dog()
    D.setName("J")
    D.setAge(6)
    D.setColor("Brown")
    D.display()

main()
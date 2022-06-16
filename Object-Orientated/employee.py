class Employee:
    """This is a class to test the isinstance function"""

    #The isistance function is used to see if something is an object and if it isn't it will be returned as false

    __slots__ = ["name", "age", "salary"]

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Gender:

    __slots__ = ["position", "gender"]

    def __init__(self, position, gender):
        self.position = position
        self.gender = gender

def main():
    emp = Employee("Em", 24, 100)
    per = Gender("Manager", "Female")
    print(isinstance(emp, Employee))
    print(isinstance(per, Gender))

main()

class Car:

    """An object created for a test and practice """

    __slots__ = ["brand", "price", "color"]

    #Costum constructor 

    def __init__(self, brand, price, color): 
        self.brand = brand
        self.price = price
        self.color = color

def main():
    car1 = Car("Honda", 100, "Blue")
    print(car1.brand, car1.price, car1.color)
    
main()
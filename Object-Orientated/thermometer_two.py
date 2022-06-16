#Creating a thermometer using object orientated programming 

class Thermometer:

    __slots__ = ["__temperature"]

    def __init__(self, temperature):
        self.__temperature = temperature

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, Temp):
        self.__temperature = Temp

    def conversion(self, units, in_temp):

        units = input("Enter the letter for conversion: ") 

        Temp = in_temp

        if units == "F":
            Temp = ((Temp - 32) * 5/9) #Fahrenheit to celsius
        elif units == "C":
            Temp = ((Temp * 9/5) + 32) #Celsius to fahrenheit
        elif units == "K":
            Temp = ((Temp + 273.15)) #Kelvin conversion works for both C and F
        else:
            print("Please enter the right unit")

    def __str__(self):
        return "Temperature: " + str(self.getTemperature()) + str(self.conversion(self.getTemperature()), "F") + "F" + str(self.conversion(self.getTemperature), "C") + "C" + str(self.conversion(self.getTemperature), "K") + "K"

def main():

    input_temp = (input("Enter the temp: "))  
    Weather = Thermometer(input_temp)
    in_temp = Weather.getTemperature()
    Weather.conversion(in_temp)
    print(Weather.__str__())

main()
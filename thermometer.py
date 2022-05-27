#Convert create a thermometer

def temperature_convert(): 

    letter = input("Enter the sign of choice for convertion: ")

    if letter == 'C': 
        celsius = int(input("Enter celsius temperature: "))
        print((celsius * 9/5) + 32) #Convert celsius to fahrenheit 
    elif letter == 'F':
        fahrenheit = int(input("Enter fahrenheit temperature: "))
        print((fahrenheit - 32) * 5/9) #Convert fahrenheit to celsius 
    elif letter == 'K':
        celsius = int(input("Enter celsius temperature: "))
        fahrenheit = int(input("Enter fahrenheit temperature: "))
        print("Celsius:", (celsius + 273.15)) #Convert celsius to kelvin 
        print("Fahrenheit:", ((fahrenheit + 459.67) * 5/9)) #Convert celsius to kelvin

def main():
    temperature_convert()

main()
import os

def clearscreen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def mainMenue():
    clearscreen()
    print("Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Temperature converter")
    print("2. Distence converter ")
    choice = int(input("Enter your choice 1,2 ---- :"))
    clearscreen()
    match choice:
        case 1:
            Temperatureconverter()
        case 2:
            Distenceconverter()
        case _: 
            print("Please enter correct input")
            mainMenue()
def Temperatureconverter():
    print("1. Convert Celsius ↔ Fahrenheit")
    print("2 Convert Fahrenheit ↔ Celsius")
    choice = int(input("Enter your choice 1,2 ---- :"))
    inputtemp = float(input("enter tempurature")) 

    match choice:
        case 1:
            outvalue= inputtemp * (9/5) +35
            print(f'{inputtemp} C = {outvalue} F')
        case 2:
            outvalue= (inputtemp  - 35) * (5/9)
            print(f"{inputtemp} F = {outvalue} C")
        case _: 
            print("Please enter correct choise")
            exit()
        
def Distenceconverter():    
    print("1. Convert km ↔ mile")
    print("2 Convert mile ↔ km")
    choice = int(input("Enter your choice 1,2 ---- :"))
    inputtemp = float(input("enter tempurature")) 
    match choice:
        case 1:
            outvalue = inputtemp * 0.621371
            print(f"{inputtemp} mk = {outvalue} miles")
        case 2:
            outvalue = inputtemp * 1.609344
            print(f"{inputtemp} miles = {outvalue} km")
        case _: 
            print("Please enter correct choise")
            exit()
               
    
mainMenue()    
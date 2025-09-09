import os
import ast
def clearscreen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def mainMenue():
    clearscreen()
    print("Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)\n")
    
    

    choice = int(input("Enter your choice 1,2,3,4 ----"))

    clearscreen()

    print(choice)
    match choice:
        case 1: 
            print("you seleted  Addition (+)")
        case 2: 
            print("you seleted Subtraction (-)")
        case 3: 
            print("you seleted Multiplication(*)")
        case 4: 
            print("you seleted Division(/)")
        case _: 
            print("Pleease select correct option ")   
            input("Press any key")
            # mainMenue()
    inputval = input("Enter first number: ")     
    match eval(inputval):    
        case int():
            imput1 = int(inputval)
        case float():
            imput1 = float(inputval)    
        case _:
            print("Pleease entery valied number ")   
            input("Press any key")
            # mainMenue()
    inputval2 = input("Enter second number: ")   
    
    match eval(inputval2):    
        case int():
            imput2 = int(inputval2)
        case float():
            imput2 = float(inputval2)    
        case _:
            print("Pleease entery valied number ")   
            input("Press any key")
            exit()       
                        
    match choice:
        case 1: 
            print(f"the addition of {imput1} + {imput2} is {imput1 + imput2}")
        case 2: 
            print(f"The Subtraction {imput1} - {imput2} is { imput1 - imput2 }")
        case 3: 
            print(f"The Multiplication {imput1} * {imput2} is { imput1 * imput2 }")
        case 4: 
            print(f"The seleted Division {imput1} / {imput2} is { imput1 / imput2 }")
    print("thanks for using Simple Calculator")    
    

mainMenue()    

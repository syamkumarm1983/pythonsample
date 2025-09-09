import random
import os
def guesstheNumber():
    if os.name == 'nt':
        os.system('cls') #for windows
    else:
        os.system('clear')
    print("Guess the number from 1 to 100")
    sysnumber = random.randint(1,100)    
    noofguess = 0
    while True:
        numberguessed = int(input('Guess...  : '))
        noofguess +=1
        if numberguessed > sysnumber:
            print("Your guess is bigger than expected")
        elif numberguessed < sysnumber:
             print("Your guess is smaller than expected")
        else:
            print(f'You gessed in {noofguess} attempts')     
            break

guesstheNumber()        
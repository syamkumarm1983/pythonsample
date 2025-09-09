import os
def isPalindrome(giventest):
    #remove spaces
    newtest = giventest.lower().replace(" ","")
    return newtest == newtest[::-1]

if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')

myinput = input('Please enter string to check :')    
output =   myinput+" is palendrom "  if isPalindrome(myinput)  else myinput+"  is not palendrom "
print(output)
import os
import re
def mywordcount(givenstr):
   return givenstr.count(' ')+1

def mycharcount(givenstr):
   return len(givenstr)

def mysentences(givenstr):
       return len(re.findall("[.?!]",givenstr))

if os.name == 'nt':
   os.system('cls')
else:
   os.system('clear')
givenstr = input('enter string for counting :')

print(f"no of sentences {mysentences(givenstr)}\nno of words {mywordcount(givenstr)} and \nnof of chars {mycharcount(givenstr)}")
      

   
     
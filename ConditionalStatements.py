#simple if
age = 30
if age > 20:
    print('the given age is grate than 20')
#if-else
if age > 30:
    print(f'the given age {age} is grate than 30')
else:
    print(f"the given age {age} is equal or leassthan 30")

#if-elif-else
if age > 30:
     print(f'the given age {age} is grate than 30')
elif age == 30:
     print(f'the given age {age} is equal to 30')    
else:
     print(f'the given age {age} is leassthan 30')  

# One-line
if age > 20 : print('the given age is grate than 20')

#Ternary Operator
message = " grate than 20 " if age > 20  else " less or equal to 20" 
print('the age is '+message)

# def sampleswitch(code):
#     match code:
#         case 30:
#             return 'its 30'
#         case 31:
#             return 'its 31'
#         case 32:
#             return 'its 32'

# print(sampleswitch(age))              

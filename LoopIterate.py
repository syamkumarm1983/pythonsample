#for
frutes={'Apple','Banana','Grape'}
for frute in frutes:
    print(frute)

for i in range(5):
    print(i)

person = {"name":"syam","role":'Engineer', "age":40}    
for key,valu in person.items():
    print(f'{key} {valu}')

for i in range(5):
    print(i)
else:
    print(' the loope complted with out break')    

count = 1
while count < 4:
    print(f' count is {count}')
    count += 1
print('While is complted')

while True:
    print('this sample break in while')
    break;

print('While is complted')
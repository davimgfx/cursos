from time import sleep
from random import randint

for c in range(10,-1,-1): 
    print(f'{c} segundos!')
    sleep(1)
print('Feliz ano NOVO!')
for i in range(1,45):
    print('')

s= ''

for i in range(1,1000):
    count = randint(1,100)
    while (count > 0):
        s += ' '
        count -= 1

    if ( i % 10 ==0):
        print(s + "Feliz ano novo!")
    else:
        print(s + '*')
        
    s=''
    sleep(0.3)
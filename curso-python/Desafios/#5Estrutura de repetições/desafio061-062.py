a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n=1
extra = 1

'''extra = 1'''
'''total = 0'''

while (n < 11):
    print(f'{n}° termo da PA: {a1}', end='\n' )
    a1 += r
    n += 1
    
while (extra != 0):
        extra = int(input('Termos extras: '))
        for i in range (n,n+extra):
            print(f'{n}° termo da PA: {a1}', end='\n' )
            a1 += r
            n += 1

         
'''while (extra != 0):
    total = total + extra
    while(n <= total):
        print(f'{n}° termo da PA: {an}', end='\n' )
        an += r
        n += 1
    extra = int(input("Quantos termos vocè quer mostra extra?"))'''
    
     
print('Fim do programa!')
print(f'Aparecendo {n-1} termos da PA!')
    
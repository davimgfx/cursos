'''num1 = int(input('Digite uma valor: '))
s = 1
for i in range (num1, 0, -1):
    s *= i
print(f'O fatorial de {num1} é igual a {s}')'''



num2 = int(input('Digite uma valor: '))
f = 1
c = num2
while c > 0:
    f *= c
    print (c, end = '')
    print(' x ' if c > 1 else ' = ', end=' ')
    c -= 1
print(f)
print(f'O fatorial de {num2} é igual a {f}')




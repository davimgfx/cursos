count = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores: {tupla}')
print(f'Quantidade de 9 digitados: {tupla.count(9)}')
if 3 in tupla:
    print(f'O primeiro 3 foi digitado na posição: º {(tupla.index(3)+1)}')
else:
    print('Não há número 3 na tupla!')

print('Os valores pares foram:', end='')  
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
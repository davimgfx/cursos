n=input('Digite um número inteiro de 0 até 9999: ')
m=f'{n:0>4}'
print(f'Unidade: {m[3]}\nDezena: {m[2]}\nCentena: {m[1]}\nMilhar: {m[0]}')
print(m)
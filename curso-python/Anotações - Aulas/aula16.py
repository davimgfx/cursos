#lanche = () [] {} 
#tupla, lista e dicionario
'''
lanche2 = (int,str,str)
numero = int(input('Digite um numero: '))
texto1 = str(input('Digite o Texto 1: '))
texto2 = str(input('Digite o Texto 2: '))

lanche2 = (numero,texto1,texto2)
print(lanche2)
'''
count = 0
lanche = ('hamburguer','suco','cafe', 'pizza')
print(lanche)
print(len(lanche))
print(lanche[1:])
print(lanche[2:])
print(lanche[:2])
print(lanche[::-1])
print("----------")
for i in lanche:
    print(i)
    count += 1
print("----------")
for i in range(0, len(lanche)):
    print(lanche[i])
print("----------")
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
print("----------")
print(sorted(lanche))
print("----------")
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(5,1))
#del(c)
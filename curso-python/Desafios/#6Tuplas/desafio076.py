import os
n = int(input("Quantos números serão lidos? "))
lista = ()

for i in range(n):
     x = str(input("Digite o nome do produto: ")).strip().upper()
     y = float(input("Digite o preço do produto R$"))
     lista += tuple([x,y])
os.system("cls")     

print("--------------LISTA DE COMPRAS--------------")
for i in range (0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end ='')
    else:
        print(f'R${lista[i]:>8.2f}')
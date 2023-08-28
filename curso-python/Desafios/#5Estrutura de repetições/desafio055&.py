maior = 0
menor = 0
for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}º pessoa: '))
    if peso > maior:
        maior = peso
    if menor == 0 or peso < menor:
        menor = peso
    
print(f'Considerando os valores informados, o maior peso foi: {maior} e o menor peso foi: {menor}')



    


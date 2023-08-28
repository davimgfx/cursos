s = 0
count = 0
for i in range(0,6):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0 :
        s += num
        count += 1
if count > 1:
    print(f'Foram somados {count} números pares, e soma é igual a {s}')
elif count == 1:
    print(f'Você digitou apenas um valor par, portanto a soma é ele mesmo = {num}')
else:
    print('Você digitou 0 valores pares! Tente dinovo')     

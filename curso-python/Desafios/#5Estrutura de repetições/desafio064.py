'''num = soma = count = 0
while num != 999:
   num = int(input("Digite um número inteiro (condição de parada 999): "))
   count += 1
   soma += num
   if num == 999:
        soma -= 999
print(f'Você digitou {count-1} números inteiros e a soma entre eles é igual: {soma}')'''

num = soma = count = 0
while num != 999:
    num = int(input("Digite um número inteiro (condição de parada 999): "))
    if num != 999:
        count += 1
        soma += num
print(f'Você digitou {count} números inteiros e a soma entre eles é igual: {soma}')
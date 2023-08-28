n = s = count =0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    count += 1
print(f'Você digitou {count} números, e a soma deles é igual a {s}')
print('Acabou')
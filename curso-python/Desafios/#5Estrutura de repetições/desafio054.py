from datetime import date 
anoatual = date.today().year
count = 0

for i in range(1,8):
    nasc = int(input(f'Digite o ano de nascimento da {i}º: '))
    if anoatual - nasc < 21:
        count += 1

print(f'Quantidade de pessoas que atingiram a maioridade: {7-count}')
print(f'Quantidade de pessoas que NÃO atingiram: {count}')
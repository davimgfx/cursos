opcao = 'A'
maior = menor = s = count = 0
while opcao not in ['N']:
    num = int(input('Digite um número: '))
    opcao = str(input('Você deseja continuar? ')).strip().upper()
    s += num
    count += 1
    if num > maior:
        maior = num
    elif menor == 0 or num < menor:
        menor = num
print(f'Foram digitados {count} números, sendo o maior {maior} e o menor {menor}')
print(f'A media deles foram {s/count:.2f}')
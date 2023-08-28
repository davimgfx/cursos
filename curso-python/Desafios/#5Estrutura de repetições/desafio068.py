from random import randint
count = -1
while True:
    print('-=-' * 20)
    cpu = randint(0,10)
    user = int(input('Digite um número inteiro: '))
    print('-=-' * 20)
    opcao = ' '
    while opcao not in ['PAR','IMPAR']:
        opcao = str(input('Você escolhe par ou impar? ')).strip().upper()
    print('-=-' * 20)
    soma = user + cpu
    count += 1
    print(f'Você colocou {user} e o Cpu {cpu}:\n{user} + {cpu} = {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if opcao in ['PAR']:
        placar = 'Par'
        if soma % 2 == 0:
            print("Vitoria do usuário! Mais uma rodada!")
        else:
            print('Derrota!')
            break
    if opcao in ['IMPAR']:
        placar = 'Ímpar'
        if soma % 2 != 0:
            print("Vitoria do usuário! Mais uma rodada!")
        else:
            print('Derrota! Tente de novo!')
            break
   
print(f'Você venceu {count} o computador!')
print('-=-' * 20)
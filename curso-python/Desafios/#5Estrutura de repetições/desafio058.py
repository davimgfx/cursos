from random import randint
from time import sleep
count = 1

numc = randint(0, 10)
print('-=-' * 20)
numu = int(input('Adivinhe um número entre 0 e 10: '))
print('-=-' * 20)
print(' ' * 20, 'CHANCES DE 10%')
print('-=-' * 20)
print(' ' * 22,'CARREGANDO...')
sleep(1)


while numu != numc:
    numu = int(input("   TENTE DE NOVO! Digite um número entre 0 a 10: "))
    print('-=-' * 20)
    print(' ' * 22,'CARREGANDO...')
    sleep(1)
    count += 1

if numc == numu:
    print('-=-' * 20)
    print(' ' * 18, f'Numero sorteado: {numc}')
    print(' ' * 20, 'Usuário Venceu!')
    if count == 1:
        print(' ' * 18, "De primeira que sorte!")
    else:
        print(' ' * 20, f"Com 5 tentativas!")


print('-=-' * 20)  
print(' ' * 22,'FIM DO JOGO')
print('-=-' * 20)

from emoji import emojize
from random import choices
from time import sleep

r = 'S'
countpes = 0
countcpu = 0
while r == 'S':
    print('-=-' * 20)
    pessoa = str(input('Escolha: PEDRA, PAPEL OU TESOURA: ')).replace(" ","").upper()
    print('-=-' * 20)

    opcao = ['PEDRA', 'PAPEL', 'TESOURA'] 
    cpu = choices(opcao)

    if pessoa in opcao:
        print(' ' * 20,'CARRENGANDO...')
        sleep(1)
        print(' ' * 23,'\033[1;32mJO\033[m')
        sleep(1)
        print(' ' * 25,'\033[1;33mKEN\033[m')
        sleep(1)
        print(' ' * 28,'\033[1;31mPÔ\033[m')
        sleep(2)
        print(' ' * 3,f"USUÁRIO colocou {pessoa} x CPU colocou {''.join(cpu)}")

    if pessoa == 'PEDRA':
        if cpu == ['PEDRA']:
            print(emojize('                       :raised_fist: x :raised_fist:'))
            print('\033[1;33m                       EMPATE\033[m')
        elif cpu == ['PAPEL']:
            print(emojize('                       :raised_fist: x :hand_with_fingers_splayed:'))
            print('\033[1;31m                   VITORIA DO CPU\033[m')
            countcpu += 1
        else:
            print(emojize('                       :raised_fist: x :victory_hand:'))
            print('\033[1;32m                  VITORIA DO USUARIO\033[m')
            countpes += 1
        print(' ' * 18,f'PLACAR DO JOGO')
        print(' ' * 23,f'{countpes} x {countcpu}')

    elif pessoa == 'PAPEL':
        if cpu == ['PEDRA']:
            print(emojize('                       :hand_with_fingers_splayed:  x :raised_fist:'))
            print('\033[1;32m                 VITORIA DO USUARIO\033[m')
            countpes += 1
        elif cpu == ['PAPEL']:
            print(emojize('                       :hand_with_fingers_splayed:  x :hand_with_fingers_splayed:'))
            print('\033[1;33m                       EMPATE\033[m')
        else:
            print(emojize('                       :hand_with_fingers_splayed:  x :victory_hand:'))
            print('\033[1;31m                   VITORIA DO CPU\033[m')
            countcpu += 1
        print(' ' * 20,f'PLACAR DO JOGO')
        print(' ' * 23,f'{countpes} x {countcpu}')

    elif pessoa == 'TESOURA':
        if cpu == '[PEDRA]':
            print(emojize('                          :victory_hand: x :raised_fist:'))
            print('\033[1;31m                     VITÓRIA DO CPU\033[m')
            countcpu += 1
        elif cpu == ['PAPEL']:
            print(emojize('                          :victory_hand: x :hand_with_fingers_splayed:'))
            print('\033[1;32m                     VITÓRIA DO USUARIO\033[m')
            countpes +=1
        else:
            print(emojize('                          :victory_hand: x :victory_hand:'))
            print('\033[1;33m                          EMPATE\033[m')
        print(' ' * 20,f'PLACAR DO JOGO')
        print(' ' * 25,f'{countpes} x {countcpu}')

    else:
        print(' ' * 20,'OPÇÃO INVALIDA!')
    print('-=-' * 20)
    r = str(input('Deseja continuar? (s/n): ')).upper().strip()
    print('-=-' * 20)
    if r == 'N':
        print(' ' * 20,'FIM DO JOGO')
        print('-=-' * 20)
        print(' ' * 20,'PLACAR FINAL')
        print(' ' * 16,f'USUARIO {countpes} x {countcpu} COMPUTADOR')
        print('-=-' * 20)
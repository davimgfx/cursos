from calendar import isleap
from time import sleep
from datetime import date

nasc =int(input('\n\nDigite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print("PROCESSANDO...")
sleep(1.5)
if idade <=17:
    print(f"Não precisa se alistar ainda! Você tem {idade} anos!")
elif idade == 18:
    print(f'Você precisa se alisar!Você têm {idade} anos!')
else:
    print(f'Ja passou do tempo de alistamento!Você têm {idade} anos!')
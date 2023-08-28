from calendar import isleap
from time import sleep
from datetime import date
ano = int(input('Digite um ano: '))
print('ANALISANDO...')
sleep(0.5)
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print(f'o ano de {ano} é bissexto')
else:
    print(f'o ano de {ano} NÃO é bissexto')
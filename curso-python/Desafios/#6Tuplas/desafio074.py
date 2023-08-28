from random import randint

tupla = tuple(randint(i + 1, 999) for i in range(0,5))
print(f'Lista gerada: {tupla}')
print(f'Em ordem crescente: {sorted(tupla, reverse=True)}')
print(f'Em ordem decrescente: {sorted(tupla)}')
print(f'Maior valor: {max(tupla)}')
print(f'Menor valor: {min(tupla)}')
maior = menor = total = count = 0
print('-=-' * 20)
print('Faça suas compras :)')
while True:
    print('-=-' * 20)
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto R$'))
    print('-=-' * 20)
    total += preco
    opcao = ' '
    while opcao not in ['S','N']:
        opcao = str(input('Deseja continuar? (s/n) ')).strip().upper()
    if preco > 1000:
        count += 1
    if menor == 0 or menor > preco:
        menor = preco
        menornome = nome
    if preco > maior:
        maior = preco
        maiornome = nome
    if opcao == 'N':
        break

print('-=-' * 20)
print(f'O total da compra foi igual a {total}')
print(f'{count} produtos custaram mais de R$1000')
print(f'O nome do produto mais barato é {menornome} e custou R${menor}')
print(f'O nome do produto mais caro é {maiornome} e custou R${maior}')
print('-=-' * 20)
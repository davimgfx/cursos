pessoas = homens = mulher = 0
while True:
    print('-=-' * 20)
    idade = int(input('Digite uma idade: '))
    
    sexo = ' '
    while sexo not in ['M','F']:
        sexo = str(input('Digite o sexo (m/f): ')).strip().upper()
    print('-=-' * 20)

    if idade > 18:
        pessoas += 1
    if sexo in ['M']:
        homens += 1
    if idade < 20 and sexo in ['F']:
        mulher += 1

    opcao = ' '
    while opcao not in ['S', 'N']:
        opcao = str(input('Deseja continuar (s/n): ')).strip().upper()

    if opcao in ['N']:
        print(f'Finalizando programa!')
        break

print(f'Pessoas com mais de 18 anos: {pessoas}')
print(f'Quantidade de homens cadastrados: {homens}')
print(f'Quantidade de mulheres com menos de 20 anos: {mulher}')


#cidade = str(input("Digite o nome da sua cidade: ")).strip
#print(cidade[:5].upper() == 'SANTOS')

frase=str(input('Nome da cidade: ')).strip().upper().split()
print('SANTO' in frase[0])
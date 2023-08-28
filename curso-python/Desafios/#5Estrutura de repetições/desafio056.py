media = 0
count = 0
maiorhomem = 0
for i in range(1,5):
    nome = str(input('Digite o nome: ')).title().strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input(f'Digite o sexo da pessoa (m ou f): ')).upper().replace(" ","")
    media += idade
    if idade < 20 and sexo == 'F':
        count += 1
    if maiorhomem < idade and sexo == 'M':
        maiorhomem = idade
        maiorn = nome

print(f'A média de idades do grupo é {media/4:.2f}.')
print(f'O nome do homem mais velhor é {maiorn} e ele tem {maiorhomem} anos.')
print(f'São {count} mulheres que possuem menos de 18 anos.')




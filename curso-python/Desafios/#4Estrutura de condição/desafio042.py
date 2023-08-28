from time import sleep
print("Insira os valores do comprimento de retas: ")
r1 = float(input("Digite um valor: "))
r2 = float(input("Digite um valor: "))
r3 = float(input("Digite um valor: "))
print('ANALISANDO...')
sleep(3)
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):
    print("\033[;32mTriângulo formado!\033[m")
    if r1==r2==r3:
        print("Triângulo Equilátero!Todos os lados são iguais.")
    elif r1==r2 or r1==r3 or r2==r3:
        print("Triângulo Isósceles!Dois lados iguais!")
    else:
        print("Triângulo Escaleno!Todos os lados diferentes!")
else:
    print("\033[;31mNão forma um triângulo\033[m")
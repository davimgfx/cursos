from time import sleep
print("Insira os valores do comprimento de retas: ")
r1 = float(input("Digite um valor: "))
r2 = float(input("Digite um valor: "))
r3 = float(input("Digite um valor: "))
print('ANALISANDO...')
sleep(3)
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):
    print("Triângulo formado!")
else:
    print("Não forma um triângulo")
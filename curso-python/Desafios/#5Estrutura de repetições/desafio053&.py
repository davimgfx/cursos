frase = str(input("Digite uma farase: ")).upper().replace(" ","")
print(frase)
if frase == frase[::-1]:
    print('É um Palíndromo')
else:
    print('Não É!')

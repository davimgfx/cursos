altura = float(input("Digite sua altura m: "))
peso = float(input('Digite seu peso kg: '))
imc = peso/(altura*altura)

print(f'O IMC dessa pessoa é {imc:.2f}')
if imc<18.5:
    print('Abaixo do peso normal!')
elif 18.5<=imc<=25:
    print('Peso ideal!')
elif 25<imc<=30:
    print('Sobrepeso!')
elif 30<imc<=40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')
    

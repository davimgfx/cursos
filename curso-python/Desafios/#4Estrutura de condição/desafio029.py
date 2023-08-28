km = float(input("Velocidade lida (km/h): "))
if km > 80:
    print('Vocô foi multado!')
    multa = (km-80)*7
    print(f'Valor da multa em reais: {multa:.2f}')
else:
    print("Abaixo do limite!")

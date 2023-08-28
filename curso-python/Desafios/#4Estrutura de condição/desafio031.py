viagem = float(input('Digite a distância da viagem(km): '))
#gasto = viagem*0.5 if viagem <=200 else viagem*0.45
if viagem <= 200:
    gasto = viagem*0.50
else:
    gasto = viagem*0.45
print(f"Valor da viagem em reais: {gasto}")

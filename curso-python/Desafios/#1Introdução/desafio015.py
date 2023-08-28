dias = int(input("Digite o número de dias alugados: "))
km = float(input("Digite a quantidade de km rodados: "))
total = (dias*60) + (km*0.15)
print(f"O preço a pagar é igual: {total} reais")
salario = float(input("Digite o valor do seu sálario: "))

if salario > 1250:
    aumento = salario*1.10
    print(f"Novo salário: {aumento}")
else:
    aumento = salario*1.15
    print(f'Novo salário: {aumento}')

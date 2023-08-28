from time import sleep

valor = float(input('\n\n\033[4;33mDigite o valor da casa:\033[m R$'))
salario = float(input('\033[4;33mDigite o salário:\033[m R$'))
anos = float(input('\033[4;33mDigite a quantidade de anos para pagar a casa:\033[m '))
mensal = valor/(anos*12)

print("PROCESSANDO...")
sleep(3)

print(f'Para pagar uma casa de \033[;32mR${valor}\033[m em \033[;32m{anos}\033[m anos, a prestação mensal será de \033[;32mR${mensal:.2f}\033[m')
if mensal <= salario*0.30:
    print("\033[;32mAcesso permitido!\033[m")
else:
    print(f'\033[;31mAcesso Negado!\033[m\n\n')


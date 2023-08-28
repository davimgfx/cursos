from time import sleep
preco = float(input('\nDigite o valor do produto: R$'))
forma = int(input('Você deseja pagar com:\n[1]No dinheiro \n[2]No cartão \n[3]Pix\n'))
print(f"CARREGANDO")
sleep(2)
if forma == 1 or forma == 3:
    print(f'Você recebe 10% de desconto, e o produto fica com R${preco*0.90:.2f}')
if forma == 2:
    cartao = int(input('Voce deseja parcelar:\n[1]Nenhuma \n[2]2 vezes \n[3]3 ou mais vezes\n'))
    if cartao == 1:
        print(f'Você recebe 5% de desconto, e o produto fica com R${preco*0.95:.2f}')
    elif cartao == 2:
        print(f'Preço normal R${preco}')
    elif cartao == 3:
        print(f'Voce terá que pagar 20% de juros a cada mês, e o pruduto fica com R${preco*1.20:.2f} ')
    else:
        print('Seleção Não Valida!')
else:
    print('Opção Inválida!')
    


   
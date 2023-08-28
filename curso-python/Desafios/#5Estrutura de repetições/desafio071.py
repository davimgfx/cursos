while True:
    valor = int(input("informe o valor a ser sacado R$"))
    nota50 = valor //50
    valor %= 50
    nota20 = valor //20
    valor %= 20
    nota10 = valor //10
    valor %= 10
    nota1 = valor //1
    print(f'{nota50} de R$50\n{nota20} de R$20\n{nota10} de R$10\n{nota1:.1f} de R$1')
    opcao =' '
    while opcao not in ['S','N']:
        opcao = str(input("Deseja repetir a operação?(s/n) ")).strip().upper()
    if opcao in ['N']:
        print('FIM DO PROGRAMA!')
        break
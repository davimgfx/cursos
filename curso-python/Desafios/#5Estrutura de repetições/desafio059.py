n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

menu = 0

while menu != 5:
    print('======MENU======')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    print('=================')
    menu = int(input('Escolha uma operação: '))
    if menu == 1:
        oper = n1 + n2
        print(f"A soma entre {n1} e {n2} é {oper}")
    elif menu == 2:
        oper = n1 * n2
        print(f"A multiplicação entre {n1} e {n2} é {oper}")
    elif menu == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        elif n1 < n2:
            print(f"{n2} é maior que {n1}")
        else:
            print(f"Os números são iguais")
    elif menu == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif menu == 5:
        print('FIM DO PROGRAMA!')
    else:
        print('Opção INVÁLIDA!Tente Novamente')
   
    
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
 'seis', 'sete', 'oito', 'nove', 'dez', 'once', 'doze', 
 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete','dezoito',
 'dezenove','vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num  <= 20:
        print(extenso[num])
        opcao = ' '
        while opcao not in ['S','N']:
            opcao = str(input('Deseja continuar? (s/n): ')).strip().upper()
        if opcao in ['N']:
            print('Saindo do programa')
            break 
    
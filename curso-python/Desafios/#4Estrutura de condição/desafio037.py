num = int(input("Digite um numero inteiro qualquer: "))
conversao = int(input('Conversão:\n1 - Para binário\n2 - Para octal\n3 - Para hexadecimal\n'))
if conversao == 1:
    print(f"{bin(num)}")
elif conversao == 2:
    print(f"{oct(num)}")
elif conversao == 3:
    print(f"{hex(num)}")  
else:
    print("\033[;31mBase de conversão não encontrada!Tente novamente!\033[m")
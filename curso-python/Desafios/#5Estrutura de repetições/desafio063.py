print("Sequência de Fibonacci: ")
num = int(input('Digite um número inteiro: '))
t1 = 0
t2 = 1
count = 3
extra = 1
if num == 1:
    print(f"O 1º da Sequência de Fibonacci é igual a 0")
elif num == 2:
    print(f"O 1º da Sequência de Fibonacci é igual a 0")
    print(f"O 2º da Sequência de Fibonacci é igual a 1")
else:
    print(f"O 1º da Sequência de Fibonacci é igual a 0")
    print(f"O 2º da Sequência de Fibonacci é igual a 1")
    while (num+1 != count):
        t3 = t2 + t1
        print(f"O {count}º da Sequência de Fibonacci é igual a {t3}")
        t1 = t2
        t2 = t3
        count += 1

opcao = str(input('Deseja ver mais termos (s/n)? ')).strip().upper()

if opcao not in ['S','N']:
    while opcao not in ['S','N']:
        opcao = str(input('Opção inválida! Digite (s/n): ')).strip().upper()

elif opcao in ['N']:
    print('OK!')

elif opcao in ['S']:
    while (extra != 0):
        extra = int(input('Termos extras: '))
        for i in range(count, count+extra):
            t3 = t2 + t1
            print(f"O {count}º da Sequência de Fibonacci é igual a {t3}")
            t1 = t2
            t2 = t3
            count += 1

print("FIM DO PROGRAMA")
count = 0
while True:
    num = int(input("Digite um numero inteiro positivo: "))
    if num < 0:
        break
    print("------Tabuada------")
    for i in range(0, 11):
        print(f'{num} x {i} = {i*num}')
    count += 1
    print("-------------------")
print (f'Você digitou {count} números')


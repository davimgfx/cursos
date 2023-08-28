n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua primeira nota: '))
m = (n1+n2)/2
if m>=7:
    print(f'Você esta aprovado!, media: {m:.2f}')
else:
    print(f'Se fudeu!, media: {m:.2f}')
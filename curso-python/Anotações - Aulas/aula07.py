n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s= n1 + n2
m = n1 * n2
df = n1 / n2
di = n1 // n2
e1 = n1 ** n2 
e2 = pow(n1,n2)
n1 += 4 # n1 = n1 + 4
n1 -= 4 # n1 = n1 - 4
n1 /= 4 # n1 = n1 / 4
n1 **= 4  # n1 **= n1**4
print(f'A soma {s}\nA multiplicação {m}\nA divisão float {df:.3f}', end = " ")
print(f',a divisão inteira {di}, n1 elevado a n2 {e1} e {e2}')
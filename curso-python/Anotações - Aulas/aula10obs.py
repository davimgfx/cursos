from getpass import getpass
nome = str(input("Qual é seu nome: "))
senha = getpass("Senha: ")

#if nome in 'Bob' or 'Tom' or 'Mike:
if nome in ['Bob', 'Tom', 'Mike']:
    print("Acesso garantido!")
else:
    print("Acesso negado!")
print(senha)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = a[::-1]
c = a[::2]
print(b)
print(c)
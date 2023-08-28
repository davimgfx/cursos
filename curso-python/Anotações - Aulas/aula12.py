nome = str(input("\033[4;33mQual é o seu nome?\033[m "))
if nome == 'Davi':
    print('Prazer Davi')
elif nome == 'Pedro' or 'Maria' or 'Carlos':
    print('Seu nome é muito popular no Brasil')
elif nome in 'Ana Caroline Sampaio Melodi':
    print('Belo nome feminino')
else:
    print('Que nome legal!')
print(f"Tenha um bom dia {nome}!")
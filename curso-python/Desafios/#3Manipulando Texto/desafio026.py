frase = str(input('\033[0;33mDigite uma frase: \033[m')).strip().upper()
#print(f"Quantidade de vezes que aparece a letra 'a': {frase.count('A' + 1)}")
print(f"Quantidade de vezes que aparece a letra 'a': {frase.count('A')}")
print(f"Primeiro 'a': {frase.find('A') + 1}")
print(f"Ultimo 'a': {frase.rfind('A') + 1}")
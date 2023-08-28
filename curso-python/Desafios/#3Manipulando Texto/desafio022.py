nome = str(input("Digite seu nome: ")).strip()
nomedivido = nome.split()
print(f"Seu nome em letras maiúsculas {nome.upper()}.")
print(f"Seu nome em letras minúsculas {nome.lower()}.")
print(f"Seu nome tem {len(nome) - nome.count(' ')} caracteres.")
print(f"Seu primeiro nome é {nomedivido[0]} e possui {len(nomedivido[0])} caracteres.")



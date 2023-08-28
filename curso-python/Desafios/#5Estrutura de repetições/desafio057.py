sexo = str(input('Digite o seu sexo (m/s): ')).strip().upper()
while sexo not in ['S','M']:
    sexo = str(input('INVÁLIDO! Digite seu sexo novamente (m/s): ')).strip().upper()
print(f'Sexo {sexo} registrado!')


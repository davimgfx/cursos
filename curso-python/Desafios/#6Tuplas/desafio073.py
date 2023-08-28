seriea = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Atlético-PR',
'Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Bragantino',
'Coritiba','Cuiabá','Ceará SC','Atlético-GO','Avaí','Juventude')

print('---0---')
for i in range(0,5):
    print(f'Na posição {i+1}º{seriea[i]}')
print('---0---')
for i in range(15,20):
    print(f'Na posição {i+1}º{seriea[i]}')
print('---0---')
print(sorted(seriea))
print('---0---')
print(seriea.index('Flamengo')+1, 'º Colocado o Flamengo está')





    
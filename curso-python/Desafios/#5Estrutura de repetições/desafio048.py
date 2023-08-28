s = 0
so = 0
count = 0
'''for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        s += c
        count += 1
print(f'A soma de todos os valores: {count} é igual a {s}')
'''
for i in range(1, 501, 2):
    if i % 3 ==0:
        s += i
        count += 1
print(f'A soma de todos os valores: {count} é igual a {s}')

for i in range(3, 500, 6):
    so += i
print(so)

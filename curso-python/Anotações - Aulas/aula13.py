#o ultimo numero ele ignora 0-6 (0-5)
"""for a in range (0,6):
    print('Oi!')

for b in range (0,6):
    print(b)
"""
print("--0--")
c = 0
for c in range(5,10):
    c += 1
    print(c)
print("--0--")

#o ultimo numero ele ignora 6-1 (6-0)
for d in range (6, 0, -1):
    print (d)
print("--0--")

n = int(input('Digite um número: '))
for e in range (0, n+1):
    print(e)
print("--0--") 

inicio = int(input('Digite o começo: '))
final = int(input('Digite o final: '))
passo = int(input('Digite o passo: '))
for f in range(inicio,final+1,passo):
    print(f)
print("--0--") 

s = 0
for g in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
    print (s)
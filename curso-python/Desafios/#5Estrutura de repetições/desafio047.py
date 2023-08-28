print('Os números pares inteiros do intervalo [1,50] são:')
for i in range(2,51,2):
    print(i, end=':')
   

print('\n--0--')

for i in range(1,50):
    if i % 2 == 0:
        print(i)

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))
media = (n1 + n2)/2

print(f'Sua média final foi {media:.1f}!')
if 7 <= media <= 10:
    print(f'\033[;32mVocê está aprovado! Sua média final foi\033[m')
elif 5<= media <6.9:
    print(f'\033[;33mVocê está na recuperação! Sua média final foi \033[m')
else:
    print(f'\033[;31mVocê está reprovado! Sua média final foi \033[m')
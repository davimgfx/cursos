import random
from time import sleep

numc = random.randint(0, 5)
print("\n\n\033[0;33m=============================================\033[m")
print("\033[0;32m============---ACERTE O NÚMERO---============\033[m")
print("\033[0;33m=============================================\033[m")
numu = int(input("\033[1;35m        Digite um número de\033[m 0 \033[1;35ma\033[m 5 \033[1;35m:\033[m "))
print("\033[0;32m              CHANCES DE 16,67%              \033[m")
print('               \033[1;35m CARREGANDO...\033[m\n')
sleep(3)
if numc == numu:
    print(f"              \033[1;35mNumero sorteado :\033[m {numc}")
    print("               \033[4;1;32mUsuário Venceu!\033[m")
else:
    print(f"              \033[1;35mNumero sorteado :\033[m {numc}")
    print("              \033[4;1;31mComputador Venceu!\033[m")
print("\033[0;33m=============================================\033[m")
print("\033[0;32m===============--FIM DO JOGO--===============\033[m")
print("\033[0;33m=============================================\033[m\n\n")


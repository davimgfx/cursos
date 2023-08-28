from datetime import date 

nasc = int(input('Digite seu ano de nascimento: '))
date.today().year
ano = anoatual - nasc
if ano <= 9:
    print("Você é Mirim!")
elif ano <=14:
    print("Você é Infantil!")
elif ano <=19:
    print("Você é Junior!")
elif ano <= 20:
    print("Você é Sênior!")
else:
    print('Você é Master!')
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede que quer pintar: '))
area = largura*altura
perimetro = (largura+altura)*2
litro = area/2
print(f"\nSua área: {area}, seu perimetro: {perimetro}, a quantidade de baldes para pintar a parede {litro}l de tinta")
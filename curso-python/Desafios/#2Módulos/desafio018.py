import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"Valor do seno:{seno:.2}\nValor do cosseno{cosseno:.2}\nValor da tangente{tangente:.2}")
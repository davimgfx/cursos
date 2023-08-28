from math import hypot
a = float(input('Digite um cateto do triângulo retângulo: '))
b = float(input('Digite outro cateto do triângulo retângulo: '))
c = (a*a + b*b)**(1/2)
d = hypot(a, b)
print(f"Hipotenusa: {c:.2}, {d:.2}")
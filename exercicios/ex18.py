import math

theta = float(input('qual o valor do angulo de um triangulo qualquer: '))
angulo = math.radians(theta)

print(f'o valor do seno é {math.sin(angulo):.2f}')
print(f'o valor do cosseno é {math.cos(angulo):.2f}')
print(f'o valor da tangente é {math.tan(angulo):.2f}')
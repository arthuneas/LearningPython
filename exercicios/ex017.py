from math import pow, sqrt

co = float(input('qual o valor do cateto oposto: '))
ca = float(input('qual o valor do cateto adjacente: '))

hip = sqrt(pow(co, 2) + pow(ca, 2))
#hip = math.hypot(co, ca)

print(f'o valor da hipotenusa é: {hip:.2f}')
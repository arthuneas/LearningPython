n1 = int(input('digite o 1° reta: '))
n2 = int(input('digite o 2° reta: '))
n3 = int(input('digite o 3° reta: '))

if n1 + n2 > n3 and n3 + n2 > n1 and n3 + n1 > n2:
    print('forma triangulo')
else:
    print('não forma triangulo')
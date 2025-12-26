l1 = float(input('digite o lado 1 do triangulo: '))
l2 = float(input('digite o lado 2 do triangulo: '))
l3 = float(input('digite o lado 3 do triangulo: '))

perimetro = l1 + l2 + l3
print(perimetro)

if l1 == l2 == l3:
    print('EQUILATERO')

elif l1 != l2 and l1 != l3 and l1 != l3:
    print('ESCALENO')
    
elif l1 == l2 or l3 == l2 or l1 == l3: 
    print('ISOCELES')
vel = float(input('qual a velocidade do carro: '))

multa = (vel - 80) * 7

if vel > 80:
    print(f'VOCÊ FOI MULTADO! pagará R${multa:.2f} de multa')
    
else:
    print('velocidade regular')
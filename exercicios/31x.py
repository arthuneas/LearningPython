distance = float(input('qual a distancia em km: '))

if distance > 200:
    print(f'o valor da viagem de {distance} KM é R${distance * 0.45:.2f}')
else:
    print(f'o valor da viagem de {distance} KM é R${distance * 0.5:.2f}')
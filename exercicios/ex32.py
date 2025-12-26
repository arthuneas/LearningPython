salario = float(input('qual o seu salario: '))

if salario > 1250:
    print(f'para o valor de R$ {salario} é de R$ {salario * 1.1:.2f}')
else:
    print(f'o valor da viagem de R$ {salario} é de R${salario * 1.15:.2f}')
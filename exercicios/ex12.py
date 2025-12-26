price = float(input('digite o preco: '))
salario = float(input('digite o salario atual: '))

newPrice = price * 0.95
newsalario = salario + (salario * 15 / 100)

print(f'o novo preco é {newPrice}')
print(f'o novo salario o é {newsalario}')
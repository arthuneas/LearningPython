valor = float(input('digite o valor da casa: '))
salario = float(input('digite o valor do seu salario: '))
ano = int(input('digite em quantos anos voce quer comprar essa casa: '))

meses = ano * 12
prestacao = valor / meses
excedencia = salario * 0.30 #30/100

if prestacao <= excedencia:
    print('emprestimo aceito')
else:
    print('emprestimo negado')
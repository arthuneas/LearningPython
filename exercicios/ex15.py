days = int(input('quantos dias alugados: '))
km = float(input('quantos kms foram rodados: '))

total = (km * 0.15) + (days * 60)

print(f'preço a pagar é R$ {total:.2f} reais')

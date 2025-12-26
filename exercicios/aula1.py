n1 = (input('digite um número:'))
n2 = (input('digite um outro número:'))

print(n1.isalpha())
print(type(n1))

soma = n1 + n2

print('a somaa vale {}'.format(soma))
print('a soma vale', soma) 

#preferencia
print(f'a soma entre {n1} e {n2} vale {soma}')
a = int(input('digite o 1° numero: '))
b = int(input('digite o 2° numero: '))

if a > b:
    print(f'{a} é maior que {b}')
elif b > a:
    print(f'{b} é maior que {a}')
else:
    print(f'{a} e {b} sâo iguais')
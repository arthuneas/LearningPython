#tempo = int(input('quantos ano tem seu carro? '))
#print('carro novo' if tempo <= 3 else 'carro velho')

nome = str(input('qual é seu nome? '))
nome = nome.lower()

if nome == 'arthur':
    print('que nome bonito')
elif nome == 'julia' or nome == 'pedro':
    print('que nome feio')
elif nome in 'lucia ana jessica':
    print('ok ne, nome chatooo')
else:
    print('que nome normal ein')
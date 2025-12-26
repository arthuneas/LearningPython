from datetime import date

ano =  int(input('DIGITE O ANO DE SEU NASCIMENTO: '))
atual = date.today().year

delta = atual - ano

if delta <= 9:
    print('MIRIM')

elif delta <= 14:
    print('INFANTIL')

elif delta <= 19:
    print('JUNIOR')
    
elif delta <= 20:
    print('SENIOR')
    
else:
    print('MASTER')
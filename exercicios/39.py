import datetime

born = int(input('digite o ano do seu nascimento: '))

year = datetime.date.today().year
age = year - born
limit = age - 18


if limit == 0:
    print('hora de se alistar')

elif limit > 0:
    print(f'seu alistamento excedeu em {limit} ano{"s" if limit > 1 else ""}')

else:
    #limit = abs(limit)
    limit = -limit
    if limit == 1:
        print(f'falta {limit} ano para o seu alistamento')
    else:
        print(f'faltam {limit} anos para o seu alistamento')
    
    
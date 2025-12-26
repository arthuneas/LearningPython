nome = input('digite seu nome completo: ')

nome = nome.upper().strip()
verificate = 'SILVA' in nome

nome = nome.title().split()

if verificate:
    print(f'a pessoa {nome[0]} tem silva no nome')
else:
    print(f'a pessoa {nome[0]} não tem silva no nome')
cidade = input('digite uma cidade: ')

dividido = cidade.upper().strip().split()

print('SANTO' in dividido[0])

if ('SANTO' in dividido[0]) == True:
    print(f'a cidade {cidade} começa com santo.')
else:
     print(f'a cidade {cidade} nâo começa com santo.')
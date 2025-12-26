frase = input('digite uma frase: ')

print(f'a quantidade de "a" nessa frase é {frase.lower().count('a')}')
print(f'ela aparece pela primeira vez na posição: {frase.find('a')}')
print(f'ela aparece pela ultima vez na posição: {frase.rfind('a')}')
notafinal = []

for i in range(2):
    nota = float(input(f'digite a nota {i + 1}: '))
    notafinal.append(nota)
    
media = sum(notafinal) / len(notafinal) 

print(f'a nota final recebida foi {media:.2f}')    

if media < 5:
    print('REPROVADO')
    
elif media < 7:
    print('RECUPERAÇÂO')
    
else:
    print('APROVADO')
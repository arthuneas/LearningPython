import math

a = int(input('digite o 1° numero: '))
b = int(input('digite o 2° numero: '))
c = int(input('digite o 3° numero: '))

print(max(a, b, c))
print(min(a, b, c))

menor = a
if a > b:
    menor = b
if b > c:
    menor = c
    
maior = a
if a < b:
    maior = b
if b < c:
    maior = c 
    
print(f'o menor número é {menor}')
print(f'o maior número é {maior}')

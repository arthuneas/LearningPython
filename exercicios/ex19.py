import math
import random

aluno = ["" for _ in range(4)]

for i in range(4):
    aluno[i] = input(f'digite o nome do aluno({i + 1}): ')
    
#for i in range(4):
#print(aluno[i])
    
sorteado = random.choice(aluno)
print(f'o aluno escolhido foi: {sorteado}')
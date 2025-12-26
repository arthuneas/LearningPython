import random

num = int(input('digite um numero: '))

sorteio =  random.randint(1, 5)

if num ==  sorteio:
    print(f'GANHOU, eu pensei em {sorteio} e você pensou em {num}')
else:
    print(f'PERDEU, eu pensei em {sorteio} e você pensou em {num}')
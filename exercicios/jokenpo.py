import random
from os import system

system('cls')

regras = {
      'TESOURA': 'PAPEL',
      'PEDRA': 'TESOURA',
      'PAPEL': 'PEDRA' 
}

print('''
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA
''')

option = int(input('DIGITE UMA OPÇÂO: '))

type = ['PEDRA', 'PEDRA', 'TESOURA']
joken = random.choice(type)
player = type[option - 1]


print(f'\nO PLAYER JOGOU {player}')
print(f'O COMPUTADOR JOGOU {joken}\n')

if player == joken:
      print('EMPATE')

else:
      if joken == 'TESOURA' and player == 'PAPEL':
            print('VOCE PERDEU')
      
      elif joken == 'TESOURA' and player == 'PEDRA':
            print('VOCÊ GANHOU')
            
      elif joken == 'PEDRA' and player == 'PAPEL':
            print('VOCÊ GANHOU')
            
      elif joken == 'PEDRA' and player == 'TESOURA':
            print('VOCÊ PERDEU')
      
      elif joken == 'PAPEL' and player == 'TESOURA':
            print('VOCÊ GANHOU')
            
      elif joken == 'PAPEL' and player == 'PEDRA':
            print('VOCÊ GANHOU')
            
if player == joken:
      print('EMPATE')

elif regras[player] == joken:
       print('VOCÊ GANHOU')
      
else:
      print('VOCÊ GANHOU')
      
      
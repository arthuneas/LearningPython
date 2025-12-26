import math
 
altura = float(input('DIGITE A SUA ALTURA: '))
peso  = float(input('DIGITE SEU PESO EM KG: '))

imc = peso / pow(altura, 2)
print(imc)

if imc < 18.5:
    print('ABAIXO DO PESO')
    
elif imc < 25:
    print('PESO IDEAL')
    
elif imc < 30:
    print('ACIMA DO PESO')
    
elif imc < 40:
    print('OBESIDADE')
    
else:
    print('OBESIDADE MORBIDA')

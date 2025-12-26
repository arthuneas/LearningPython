temp = float(input('digite a temperatura: '))
resp = input('essa temperatura está em farenheit ou celsius[c/f]: ')

if resp == 'c' or resp == 'C':
    newtemp = temp * 9/5 + 32
    print(f'a tempertura de {temp:.2f} em celsius para farenheit é: {newtemp:.2f}')
    
elif resp == 'f' or resp == 'F':
    newtemp = (temp - 32) * 5/9
    print(f'a tempertura de {temp:.2f} em farenheit para celsius é: {newtemp:.2f}')

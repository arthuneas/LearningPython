nome = input('Digite seu nome completo: ')

uppername = nome.upper()
lowername = nome.lower()
nomeinicial = nome.split()

letras = len("".join(nomeinicial))
letras = len(nome) - nome.count(' ')
    
print(uppername)
print(lowername)
print(letras)
print(nomeinicial[0])
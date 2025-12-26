print('digite 1 para binario')
print('digite 2 para octal')
print('digite 3 para hexadecimal')
print('-----------------------------------------------------')

while(1):
    conversor = int(input('digite qual operação deseja: '))
    if conversor == 1:
        print('binario')
        break

    elif conversor == 2:
        print('octal')
        break
        
    elif conversor == 3:
        print('hexadeicimal')
        break
        
    else:
        print('digite um valor válido')
import os

print(''' 
        ------------------------------------------
                   FORMA DE PAGAMENTO
        ------------------------------------------    
         
         1 - DINHEIRO OU CHEQUE
         2 - CARTÃO 
        
      ''')

valor = float(input('DIGITE O VALOR: '))
modo = int(input('DIGITE A FORMA DE PAGAMENTO: '))

os.system('cls')

if modo == 1:
    valor *= 0.9
    print(f'VOCÊ GANHOU 10% DE DESCONTO, AGORA O VALOR TOTAL É {valor:.2f}')
    
if modo == 2:
    print(''' 
        ------------------------------------------
                    PARCELAMENTO
                    
            1 - A VISTA
            2 = 2 VEZES NO CARTAO
            3 - 3X OU MAIS NO CARTAO
         ''')
    
    aws = int(input('DIGITE O PARCELAMENTO: '))
    os.system('cls')
    
    if aws == 1:
        valor *= 0.95
        print(f'VOCÊ RECEBEU UM DESCONTO DE 5%, AGORA O VALOR TOTAL É {valor:.2f}')
    
    elif aws == 2:
        print(f'O VALOR TOTAL É {valor:.2f}')
    
    elif aws == 3:
        valor *= 1.20
        print(f'VOCÊ RECEBEU UM JUROS DE 20%, AGORA O VALOR TOTAL É {valor:.2f}')
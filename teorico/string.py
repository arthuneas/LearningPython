frase = 'curso em video python'

#fatiamento de uma letra
print(frase[9])

#fatiamento por uma parte de string
#pega de a ate n - 1, nesse caso vai ser 12
print(frase[9:13])

#fatiamento em overflow, para pegar ate o final da frase
print(frase[9:21])

#fatiamento saltado
#nesse exemplo, pega de dois em dois
print(frase[9:21:2])

#pegar do inicio ate um limite
print(frase[:6])

#peda de limite ate o final
print(frase[15:])

#aqui temos um salto a partir de um ponto 9, definimos o alta de 3 em 3
print(frase[9::3])

#tamanho de string
print(len(frase))

#contagem de carater especifico em uma string
print(frase.count('o'))

#contagem delimitada, colocamos depois o parametros de fatiamento 
print(frase.count('o', 0, 13))

#informa em qual posicao comecou a porçao exposta, ou seja, a posicao de 'd'
print(frase.find('deo'))
#informa a ultima vez que o negocio aparece
print(frase.rfind('o'))
#como essa string nâo existe na frase, retorna -1
print(frase.find('android'))

#para saber se uma palavra/texto compoe uma string
print('curso' in frase)

#para trocar palavras de lugar 
print(frase.replace('python', 'android'))

#deixar tudo em maiusculo
print(frase.upper())

#deixar tudo em minusculo
print(frase.lower())

#capitalizar a frase, deixa tudo em minusculo exceto a primeira letra da frase 
print(frase.capitalize())

#deixa o inicio de cada palavra em maiuculo
print(frase.title())

#remover espaço vazios antes e depois de cada frase 
frase.strip()

#remover espaços vazios sometnte depois da string
frase.rstrip()

#remover espaços somente antes da string
frase.lstrip()

#dividir a string a partir dos espacos, formando novas strings
#ou seja, cada frase se torna uma nov astring
print(frase.split())

#para realizar juncao de splits
print('-'.join(frase))

#para cololocafr textos grandes, coloque-os em parenteses triplas
print(""" No Pygame, “abrir um arquivo” pode significar coisas diferentes, 
        porque depende do tipo de arquivo: imagem, som, fonte, etc.
        Ele não tem uma função genérica de “abrir qualquer arquivo” como o open() do Python,
        mas sim funções específicas para cada tipo de recurso.
      """)

#como no python tudo é objeto, voce pode usae essas funcoes com as strings
#aqui transformamos tudo para maiusculo e em seguidas fizemos a contagem de O maiusculo.
print(frase.upper().count('O'))

#conseguimos alterar a length da array com consulta simultanea
phase = '    lupa'
print(len(phase))
print(len(phase.strip()))

#aqui temos a divisao da array, a partir disso, mostramos a palava na posicao 0 da array
dividido = frase.split()
print(dividido[0])
#mostra a palavra na posicao dois, qual a letra da palavra na posicao 4
print(dividido[2][4])




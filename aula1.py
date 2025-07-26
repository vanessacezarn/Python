# para fazer um comentario
"""
DocStrings
para fazer um comentario em multiplas linhas
o computador lê ao contario do #
"""

''' 
tambem pode usar 
'''
# EXIBIR NA TELA

print("apenas isso para exibir na tela")
print(1234)

"""
o que esta dentro do parenteses é chamado de argumento 
para numero não é preciso usar aspas 
para string tem usar " " ou ' ' ==> TUDO que tiver dentro " " é uma string
cada print quebra a linha ao final(não precisa ficar usando \n)
para adicionar casas decimais a um numero(float) usa-se "."
boolean(boll)==> somente duas respostas possiveis ==> operadores logicos ==> True or False
"""

print(12,34, sep="-") # para mudar o tipo de separador dos argumentos
print(12,34, sep="-", end="@@") # ao inves dele quebrar linha ele adiciona @@ ao final dessa linha
print(45)

# para SABER O TIPO de dado que foi passado como argumento
print("-------")
print (type('vanessa'))
print(type(2))

# CONVERSÃO DE TIPOS DE DADOS
print('1',type('1'))
print(int('1'),type(int('1')))
print(str(9)+'b')

# VARIAVEIS
'''
armazenar algo na memoria
devem ser iniciadas com letra minuscula, pode ser seguidas de numeros e se tiver mais de uma palavra usar _
para atribuir um valor a variavel usa-se =
'''
nome_completo = 'Vanessa'
idade = 22
soma = 22 + 55
print('-----')
print(nome_completo)
print(idade)
print(soma)
print("-------")

#OPERADORES MATEMATICOS

divisao = 10 / 2.2
print(divisao)
divisao_inteira = 10 // 2.2
print(divisao_inteira)
exponencial = 2 ** 5
print(exponencial)
resto_divisao = 55 % 2
print(resto_divisao)
print('---------')

# PRECEDENCIA DE OPERADORES
'''
1º parenteses()
2º exponecial**
3º *, /, //, %
4º +, -
'''

#CONCATENAÇÃO E REPETIÇÃO
print('vanessa'+' '+'cezar') # o + esta concatenando str
print('nome:',nome_completo,';',idade,'anos') # quando tem variaveis e str tambem pode ser usado , para concatenar
print('va' * 10) # repete a str 10 vezes
print('---------------------')

#FORMATAÇÃO DAS STRINGS (f-strings)
texto = 'nome_completo tem idade'
text = f'{nome_completo} tem {idade} anos'
print(texto)
print(text)
#o f permite que a dentro da string tenha variaveis
altura=5.48755
print(f'a altura é de {altura:.2f}')# delimitar o numero de casas decimais 
print('----------------')

#LER DADOS DO TECLADO - input
nome = input('qual seu nome?')
print('seu nome é',nome)
print(f'o nome digitado é {nome}')
# o input sempre salva a variavel como str
numero = input('digite o numero ') 
#int(input('digite')) não é o mais correto mais funciona
int_num = int(numero)
 # é melhor para não quebrar o codigo 
print('------------------------')


#INTERPOLAÇÃO
nome = 'vanessa'
preco = 10000.455656
variavel = '%s, o preco é de R$%2.f'%(nome,preco)
print(variavel)
# FORMATAÇÃO - "localização na linha"
'''
{caractere: ><^quantidade}
'''
var = 'abc'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: ^5}')

#FATIAMENTO DE STRINGS
'''
fatiamento[inicio:final:passo(quanto caracteres tem que ser contados por vez)] [::]
função len ==> retorna a quantidade de caractere da str
'''
palavra = 'ola mundo'
print(palavra[4:]) #caracteres do indice 4 ate o final
print(palavra[0:6]) #caracteres do indice 0 ate o 6
print(palavra[:8:2]) #caracteres do indice 0 ate o 8 sendo mostrado a cada 2 caracteres
print(palavra[::-1])#palavra escrita de tras para frente
print(len(palavra))

# EXERCICIO
'''
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
'''
print('----------------')
nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

if nome  and idade :
    print(f'seu nome é {nome}')
    print(f'seu nome invertido  é {nome[::-1]}')
    if ' ' in  nome:
        print('seu nome contem espaços')
    else:
        print('seu nome não tem espaços')    
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra de seu nome é {nome[0]}')
    print(f'a ultima letra de seu nome é {nome[-1]}')


else:
    print('Descuple, voce deixou campos vazios')
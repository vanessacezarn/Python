'''
try ==> tentar executar o codigo
except ==> ocorreu algum erro ao tentar executar
'''
numero_str = input('digite um numero :')
try:
    print(f'digitado: {numero_str}')
    numero_float = float(numero_str)
    print('convertido')
    print(f'o dobro de {numero_str} é {numero_float * 2}')
except:
    print('isso não é um número')
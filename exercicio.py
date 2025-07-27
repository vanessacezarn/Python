"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('digite um numero: ')
try:
    num_int = int(num)
    if((num_int % 2) == 0):
        print(f'o numero {num_int} é par')
    else:
        print(f'o numero {num_int} é impar')
except:
    print('o numero digitado não é um numero inteiro')

print('----------------------------------------')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('digite a hora : ')
try:
    hora_int = int(hora)
    if hora_int>=0 and hora_int<=11:
        print('BOM DIA')
    elif hora_int >=12 and hora_int <=17:
        print('BOA TARDE')
    elif hora_int >=18 and hora_int <=23:
        print('BOA NOITE')
    else:
        print('hora digitada é inconpativel')
except:
    print('digite apenas numeros inteiros')

print('----------------------------------------')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('digite seu primeiro nome: ')
tam = len(nome)
if tam <=4:
    print('seu nome é curto')
elif tam>=5 and tam<=6:
    print('seu nome é normal')
else:
    print('seu nome é muito grande ')
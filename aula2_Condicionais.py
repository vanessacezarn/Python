# CONDICIONAIS
'''
if/   elif    /else
se/ se não se/ se não
cuidar o tab pois ele é quem define o que esta dentro da condicional e sera executado
'''
entrada = input('voce deseja "entrar" ou "sair" do programa ?')

if entrada == 'entrar':
    print('voce acessou o sistema')
elif entrada == 'sair':
    print('voce saiu do programa')
else:
    print('voce digitou uma opção invalida')

print('-------------------------')

# OPERADORES DE COMPARAÇÃO - RELACIONAIS
'''
>   maior
>=  maior ou igual
<   menor
<=  menor ou igual
==  igual
!= diferente
'''

#  OPERADORES LÓGICOS
'''
and(e), or(ou), not(não)
and - todas as condições precisam ser verdadeiras
or - se qualquer uma das condições for verdadeira toda a expressão envolvida com o operador lógico é dita verdadeira
not(!) - inverter expressções ==> True vira False e False vira True
'''
entrada = input('[E]ntrar ou [S]air? ')
senha=input('digite a senha: ')
senhaV = '123'

if entrada == 'E' or entrada == 'e' and senha == senhaV:
    print('entrando no sistema')
else:
    print('fim do programa')

if senha != senhaV:
    print('senha incorreta')

#OPERADORES in E not in
# verifica se algo esta ou não na string
nome = 'vanessa'
print('e' in nome)
print('v'not in nome)
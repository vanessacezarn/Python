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
'''
entrada = input('Entrar ou Sair')
senha=input('digite a senha')
senhaV=123

if entrada == 'e' and senha == senhaV:
    print('entrando no sistema')
else:
    print('sair do programa')
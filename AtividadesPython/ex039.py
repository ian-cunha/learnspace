# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
# com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
print('''Qual seu gênero? Escolha uma opção abaixo:
[ 1 ] MASCULINO
[ 2 ] FEMININO
''')
sexo = int(input('Sua opção: '))
if sexo == 2:
    print('Você não precisa fazer alistamento militar obrigatório.')
    exit()
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quen nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

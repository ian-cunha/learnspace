# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('Escolha uma das base para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
base = int(input('Sua opção: '))
if base == 1:
    print('{} convertido em BINÁRIO é {}'.format(num, bin(num)))
elif base == 2:
    print('{} convertido em OCTAL é {}'.format(num ,oct(num)))
elif base == 3:
    print('{} convertido em HEXADECIMAL é {}'.format(num ,hex(num)))
else:
    print('Tente novamente você escolheu uma base inexistente.')

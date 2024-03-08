# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das base para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Tente novamente, você escolheu uma opção inexistente.')

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n > 20 or n < 0:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        break
    else:
        break
print(f'Você digitou o número {extenso[n]}')

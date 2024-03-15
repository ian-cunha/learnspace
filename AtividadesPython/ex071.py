# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format('BANCO DockStar'))
print('=' * 30)
saque = int(input('Qual valor você quer sacar? R$'))
total = saque
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco DockStar!')
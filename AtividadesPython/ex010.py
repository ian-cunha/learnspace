# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere US$1,00=R$3,27

carteira = float(input('Digite o valor em reais para a conversão: R$'))
conversao = carteira / 4.95
print('US${:.2f}'.format(conversao))
# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

val_prod = float(input('Digite o valor do produto: R$'))
desconto = val_prod * 0.05
novo_val = val_prod - desconto
print('O produto com desconto fica: R${:.2f}'.format(novo_val))
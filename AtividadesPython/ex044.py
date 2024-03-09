# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
# - A vista dinheiro/cheque: 10% de desconto
# - A vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('-' * 20, 'STORE', '-' * 20)
valor = float(input('Preço das compras R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
tipo = int(input('Qual é a opção? '))
if tipo == 1:
    total = valor - (valor * 10 / 100)
    print('Sua compra de R${} vai custar R${} no final.'.format(valor, total))
elif tipo == 2:
    total = valor - (valor * 5 / 100)
    print('Sua compra de R${} vai custar R${} no final.'.format(valor, total))
elif tipo == 3:
    print('Sua compra de R${} vai custar R${} no final.'.format(valor, valor))
elif tipo == 4:
    total = valor + (valor * 20 / 100)
    print('Sua compra de R${} vai custar R${} no final.'.format(valor, total))
# Incompleto
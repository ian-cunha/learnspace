# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
# - A vista dinheiro/cheque: 10% de desconto
# - A vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:-^40}'.format(' STORE '))
valor = float(input('Preço das compras R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
tipo = int(input('Qual é a opção? '))
if tipo == 1:
    total = valor - (valor * 10 / 100)
elif tipo == 2:
    total = valor - (valor * 5 / 100)
elif tipo == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif tipo == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totparc, parcela))
else:
    total = valor
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))

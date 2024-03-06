# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
# e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem? '))

print('Viagem de {}Km'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da passagem é R${:.2f}'.format(preco))

'''
if distancia <= 200:
    preco = distancia * 0.50
    print('Viagem de {}Km'.format(distancia))
    print('Preço da passagem é R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Viagem de {}Km'.format(distancia))
    print('O preço da passagem é R${:.2f}'.format(preco))
print('Tenha uma boa viagem!')
'''
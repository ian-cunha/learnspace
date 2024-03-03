# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessário para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m½ (2 metros quadrados).

largura = int(input('Digite a largura em metros: '))
altura = int(input('Digite a altura em metros: '))
area = largura * altura
litros = area / 2
print('Quantidade de tinta necessário: {}l'.format(litros))
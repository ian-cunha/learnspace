# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessário para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m½ (2 metros quadrados).

largura = int(input('Largura da parede: '))
altura = int(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Dimensão da parede de {}x{} e sua área e de {}m²'.format(largura, altura, area))
print('Você precisa de {}l de tinta para pintar essa parede.'.format(tinta))
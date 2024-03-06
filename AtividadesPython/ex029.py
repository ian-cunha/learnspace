# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma  mensagem dizendo que ele foi multado.
# a multa vai custar R$7,00 por cada Km acima do limite.

veloc = int(input('Velocidade do carro: '))
if veloc > 80:
    print('Você foi multado!')
else:
    print('Você não foi multado!')
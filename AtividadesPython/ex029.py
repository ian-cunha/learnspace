# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma  mensagem dizendo que ele foi multado.
# a multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Velocidade que o carro passou: '))
if velocidade > 80.0:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um boa dia! Dirija com segurança!')

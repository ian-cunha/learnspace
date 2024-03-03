# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, consseno e
# tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tang = tan(rad)
print('Seno {:.2f},\nCosseno {:.2f},\nTangente {:.2f}'.format(sen, cos, tang))
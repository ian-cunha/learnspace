# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois iguais
# - Escaleno: todos os lados diferentes

print('-=-' * 20)
print('Analisando triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os sementos PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')

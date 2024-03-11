# Crie um programa que mostre na tela todos os números pares que estão no intervalo
# entre 1 e 50.

for contador in range(1, 51):
    num = contador % 2
    if num == 0:
        print(contador)

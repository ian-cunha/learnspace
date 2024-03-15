# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
# valor digitado pelo usuário. O programa será interrompido quando o número solicitado
# for negativo.

while True:
    num = int(input('Tabuada de: '))
    if num < 0:
        break
    print('=-'*8)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    print('-='*8)
print('Programa de tabuada encerrado, volte sempre!')

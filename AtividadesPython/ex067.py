# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
# valor digitado pelo usuário. O programa será interrompido quando o número solicitado
# for negativo.

num = cont = result = 0
while True:
    num = int(input('Tabuada de: '))
    if num == 999:
        break
    print('=-'*8)
    for cont in range(0,10):
        cont += 1
        result = num * cont
        print(f'{num} x {cont} = {result}')
    print('-='*8)
print('Finalizado.')

# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('Tabuada de: '))
print('-' * 15)
for tabuada in range(1,11):
    print('{} x {:2} = {}'.format(n, tabuada, n * tabuada))
print('-' * 15)

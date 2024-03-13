# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns
# termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('=' * 20)
print('Gerador de PA')
print('=' * 20)

num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' => ')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos exibidos.'.format(total))

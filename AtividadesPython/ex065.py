# Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi a maior e menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

resp = 'S'
soma = qtd = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / qtd
print('Você digitou {} números e a média foi {:.2f}'.format(qtd, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

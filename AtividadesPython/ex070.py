# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
# A) Qual e o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print('=-'*5, 'IANs STORE', '-='*5)
total = caro = barato = 0
while True:
    prod = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço R$'))
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += preco
    if preco > 1000:
        caro += 1
    if pergunta == 'N':
        break
    barato = preco
    if preco > barato:
         barato = preco
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi (PRODUTO) que custa R${barato}')

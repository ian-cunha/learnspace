# Desenvolva um programa que leia quatro valores pelo teclados e guarde-os em uma
# tupla. no final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valo 3.
# C) Quais foram os números pares.

par = 0
primeiro = int(input('Digite um número: '))
segundo = int(input('Outro número: '))
terceiro = int(input('Mais um número: '))
quarto = int(input('O último número: '))
valores = (primeiro, segundo, terceiro, quarto)
if primeiro % 2 == 0:
    par += 1
if segundo % 2 == 0:
    par += 1
if terceiro % 2 == 0:
    par += 1
if quarto % 2 == 0:
    par += 1
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 apareceu na {valores.count(3)}ª posição')
print(f'Os valores pares digitados foram {par}')

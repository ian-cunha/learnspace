# Desafio 007
# Desenvolva um programa que leia as duas notas
# de um aluno, calcule e mostre a sua média.
aluno = input('Nome do aluno:')
matematica = float(input('Qual a nota de matemática?'))
historia = float(input('Qual a nota de história?'))

media = matematica + historia / 2

print('A média de {} é {:.1f}'.format(aluno, media))
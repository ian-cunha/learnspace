# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

salario = float(input('Salário do funcionario: R$'))
aumento = salario + (salario * 15 / 100)
print('Salário atual R${}, salário atualizado com 15% de aumento: R${:.2f}'.format(salario, aumento))
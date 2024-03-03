# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

sal_func = float(input('Salário do funcionario: R$'))
aumento = sal_func * 0.15
novo_sal = sal_func + aumento
print('Salário atualizando: R${:.2f}'.format(novo_sal))
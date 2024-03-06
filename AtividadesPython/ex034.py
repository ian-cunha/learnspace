# Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Salário do funcionário atual é R$:'))
if salario > 1250:
    print('Salário com aumento de 10%, atualizado para {}'.format(salario + (salario * 10/100)))
else:
    print('Salário com aumento de 15%, atualizado para {}'.format(salario + (salario * 15/100)))

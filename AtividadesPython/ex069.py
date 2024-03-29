# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

mais18 = homem = mulher = 0
print('=-'*10)
print('CADASTRO DE USUÁRIOS')
print('=-'*10)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-='*10)
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        print('-='*2, 'FIM DO PROGRAMA', '=-'*2)
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos.')

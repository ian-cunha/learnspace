objeto = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(objeto)))
print('Só tem espaços? {}'.format(objeto.isspace()))
print('É um número? {}'.format(objeto.isnumeric()))
print('É alfabético? {}'.format(objeto.isalpha()))
print('É alfánumérico? {}'.format(objeto.isalnum()))
print('Está em maiúscula? {}'.format(objeto.isupper()))
print('Está em minúscula? {}'.format(objeto.islower()))
print('Está capitalizada? {}'.format(objeto.istitle()))
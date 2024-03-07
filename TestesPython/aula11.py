print('\033[4;30;45mHello World!\033[m')
print('\33[7;30;44mWelcome back!\033[m')

a = 3
b = 5
print('The values are \33[32m{}\033[m and \33[31m{}\033[m!'.format(a, b))

nome = 'Ian'
cores = {'limpa':'\33[m', 
        'azul':'\33[34m', 
        'amarelo':'\33[33m', 
        'blackwhite':'\33[7;30m'}

print('Hello, nice to meet you, {}{}{}!'.format(cores['blackwhite'], nome, cores['limpa']))

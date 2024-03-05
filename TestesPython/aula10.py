#nome = str(input('Qual o seu nome? '))
#if nome == 'Ian':
#    print('Bem-vindo de volta!')
#else:
#    print('Seja bem-vindo ao Python!')
#print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segudna nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Você passou, parabéns!')
else:
    print('Sinto muito, você não passou.')

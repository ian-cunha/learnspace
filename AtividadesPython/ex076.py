# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
# preços, na sequência. No final, mostre uma listagem de preços, organizando os dados
# em forma tabular.

produtos = ('Gabinete CoolerMaster', 550, 
            'Mouse AJAZZ 199', 250, 
            'Controle XBOX Series X', 620, 
            'Teclado RoyalKrudge V2', 320,
            'HeadSet JBL Quantum', 720, 
            'Cabo USB-C', 25)
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:>7.2f}')
print('-'*40)

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
# preços, na sequência. No final, mostre uma listagem de preços, organizando os dados
# em forma tabular.

produtos = ('Notebook DELL i7 9gen', 5500, 'Mouse AJAZZ 199', 250, 'Controle XBOX Series X', 620, 'Galaxy S23 Ultra', 4200, 'Nintendo SWITCH Oled', 2100, 'PS5 Slim', 4500, 'CoolerMaster Torre V2', 150, 'Cabo USB-C', 25)
cont = 0
print('-'*42)
print(f'{'LISTAGEM DE PREÇOS'}')
print('-'*42)
for cont in range(0, 15, 2):
    print(f'{produtos[cont]:30}', end='')
    print(f'R$ {produtos[cont+1]:8.2f}')
print('-'*42)

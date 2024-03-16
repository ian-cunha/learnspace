# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

tabela = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('=-'*20)
print(f'Lista de times do Campeonato Brasileiro: {tabela}')
print('=-'*20)
print(f'Os primeiros 5 são: {tabela[:5]}')
print('=-'*20)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('=-'*20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('=-'*20)
print(f'O Goiás está na {tabela.index('Goiás')}ª posição')

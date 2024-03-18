# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
        'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 
        'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 
        'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('=-'*20)
print(f'Lista de times do Campeonato Brasileiro: {times}')
print('-='*20)
print(f'Os primeiros 5 são: {times[:5]}')
print('=-'*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*20)
print(f'O Goiás está na {times.index('Goiás')}ª posição')
print('-='*20)

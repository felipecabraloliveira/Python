# Exercício 073 do curso de Python - Curso em vídeo

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

# Meu Código
print('=' * 37)
print(' ' * 5 + 'Tabela do Brasileirão 2017')
print('=' * 37)

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-Go')

print(f'\nLista de times do Brasileirão: {times}')
print('*' * 100)
print(f'\nA - Os 5 primeiros colocados são {times[0:5]}')
print('*' * 100)
print(f'\nB - Os 4 útimos e rebaixados são {times[-4:]}')
print('*' * 100)
print(f'\nC - Times em ordem alfabética: {sorted(times)}')
print('*' * 100)
print(f'\nD - A Chapecoense ficou na {times.index("Chapecoense")+1} posição '
      f'e o Corinthians ficou em {times.index("Corinthians")+1}º lugar, VAI CORINTHIANS!!!')
# Correção - Ok

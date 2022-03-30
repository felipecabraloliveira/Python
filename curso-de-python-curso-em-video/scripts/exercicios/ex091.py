# Exercício 091 do curso de Python - Curso em vídeo

#  Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#  Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
#  em ordem, sabendo que o vencedor tirou o maior número no dado.
# Meu Código
from random import randint
from time import sleep
print('=' * 37)
print(' ' * 6 + 'Jogo de Dados em Python')
print('=' * 37)
jogador = dict()
print('Jogando os dados...')
for c in range(1, 5):
    jogador[f'jogador{c}'] = randint(1, 6)
sleep(1)
print('Valores sorteados:')
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('\nAnalisando o vencedor...')
sleep(1)
print('*' * 15, 'Resultado', '*' * 14)

cla = 1
for i in sorted(jogador, key=jogador.get, reverse=True):
    print(' ' * 3, f'{cla}° Lugar: {i} com {jogador[i]} pontos.')
    cla += 1
print('*' * 15, '   FIM   ', '*' * 14)

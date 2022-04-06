# Exercício 092 do curso de Python - Curso em vídeo

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato.
print('=' * 37)
print(' ' * 3 + 'Cadastro de Jogador de Futebol')
print('=' * 37)

jogadores = dict()
gols = list()
jogadores['Nome'] = str(input('Nome: ').title().strip())
partidas = int(input(f'Quantas partidas {jogadores["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele arcou na partida {c}: ')))
jogadores['Gols'] = gols[:]
jogadores['Total'] = sum(gols)
print('=' * 37)
print(jogadores)
print('=' * 37)
for k, v in jogadores.items():
    print(f'{k}: {v}')
print(f'O jogador {jogadores["Nome"]} jogou {len(jogadores["Gols"])} partidas.')
print('=' * 37)
for k, v in enumerate(jogadores['Gols']):
    print(f'Na partida {k} fez {v} gols.')
print(f'Foi um total de {jogadores["Total"]} gols.')

# Exercício 089 do curso de Python - Curso em vídeo

#  Crie um programa que leia nome e duas notas de vários alunos e guarde
#  tudo em uma lista composta. No final, mostre um boletim contendo a média de
#  cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Boletim com listas compostas')
print('=' * 37)

dados = list()
alunos = list()
cont = 1
while True:
    dados.append(cont)
    dados.append(str(input('Nome do Aluno: ').strip().upper()))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[2] + dados[3]) / 2)
    alunos.append(dados[:])
    dados.clear()
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
    if continuar in 'N':
        break
print('*' * 37)
print('No.  Nome        Média')
print('-' * 22)
for i, v in enumerate(alunos):
    print(f'{alunos[i][0]:<4} {alunos[i][1]:<11} {alunos[i][4]:<4}')
vernota = 0
while True:
    print('*' * 50)
    vernota = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if vernota == 999:
        break
    for i, v in enumerate(alunos):
        if i == vernota - 1:
            print(f'Notas de {alunos[vernota-1][1]} são {alunos[vernota-1][2]} e {alunos[vernota-1][3]} com '
                  f'média de {alunos[vernota-1][4]}')
        print('Volte sempre!!!')

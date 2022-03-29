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
    print(f'{alunos[i][0]:<4} {alunos[i][1]:<11} {alunos[i][4]:>4}')
vernota = 0
while True:
    print('*' * 50)
    vernota = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if vernota == 999:
        break
    if vernota <= len(alunos):
        for i, v in enumerate(alunos):
            if i == vernota - 1:
                print(f'Notas de {alunos[vernota-1][1]} são {alunos[vernota-1][2]} e {alunos[vernota-1][3]} com '
                      f'média de {alunos[vernota-1][4]}')
    else:
        print('Aluno não encontrado, tente Novamente!')
print('Volte sempre!!!')

# outra Forma:
print('\n Outra forma')
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2 / 2)
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer Continuar? [S/n] '))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

# Exercício 090 do curso de Python - Curso em vídeo

#  Faça um programa que leia nome e média de um aluno, guardando também a
#  situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Dicionário em Python')
print('=' * 37)
aluno = dict()
aluno['Nome'] = str(input('Digite o nome do Aluno: ')).title().strip()
aluno['Media'] = float(input('Digite a média do Aluno: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação!'
else:
    aluno['Situação'] = 'Reprovado!'
print('*' * 37)
print(f'Nome: {aluno["Nome"]}\n'
      f'Média: {aluno["Media"]}\n'
      f'Situação: {aluno["Situação"]}')

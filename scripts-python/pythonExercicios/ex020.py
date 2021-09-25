# Exercicio 020 do curso de Python - Curso em vídeo

# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que ajude ele, lendo o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample, shuffle

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

print('A ordem de apresentação é a seguinte: {}'.format(sample([aluno1, aluno2, aluno3, aluno4], k=4)))

# Correção - Utilizar o método shuffle

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação é a seguinte: ')
print(lista)

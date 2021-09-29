# Exercicio 019 do curso de Python - Curso em vídeo

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# Meu código com o aprendizado até o momento:

from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
print('O aluno sorteado foi {}'.format(choice([aluno1, aluno2, aluno3, aluno4])))

# Correção - Ok
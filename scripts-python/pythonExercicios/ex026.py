# Exercicio 026 do curso de Python - Curso em vídeo

# Crie um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes aparece a letra 'A'
# 2 - Em que posição ela aparece a primeira vez.
# 3 - Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: '))
print('Quantas vezes a letra A Aparece na frase: {}'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição: {}'.format(frase.upper().find('A')))
print('A letra A aparece pela última vez na posição: {}'.format(frase.upper().rfind('A')))
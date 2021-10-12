# Exercício 038 do curso de Python - Curso em vídeo

# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
from time import sleep
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 30)
print(' ' * 4 + 'Comparando números!')
print('*' * 30)
v1 = int(input('Digite o primeiro valor? '))
v2 = int(input('Digite o segundo valor? '))
print('Primeiro valor digitado foi o {} e o segundo valor digitado foi o {}.'.format(v1, v2))
print('Comparando...')
sleep(1)
if v1 > v2:
    print('O {}primeiro{} valor é MAIOR! {} é maior do que {}.'.format(cores['g'], cores['remove'], v1, v2))
elif v2 > v1:
    print('O {}segundo{} valor é MAIOR! {} é maior do que {}.'.format(cores['blue'], cores['remove'], v2, v1))
else:
    print('Não existe valor maior, os dois são IGUAIS! {} é igual a {}.'.format(v1, v2))
# Correção - Ok

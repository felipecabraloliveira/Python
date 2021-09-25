# Exercicio 016 do curso de Python - Curso em vídeo

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção
# inteira.

from math import trunc
num = float(input('Digite um número: '))
print('O número {:.4f} possui a porção inteira de: {}.'.format(num, trunc(num)))

# Correção - Ok
print('\nOutra forma:\n O número {:.4f} possui a porção inteira de: {}.'.format(num, int(num)))

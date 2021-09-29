# Exercicio 017 do curso de Python - Curso em vídeo

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot
op = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
comp = sqrt((op ** 2) + (adj ** 2))
print('O comprimento da hipotenusa é: {:.2f} '.format(comp))

# Correção - OK
print('\nOutra forma: Realizando o cálculo utilizando o método hypot (comp = hypot(op, adj))')
comp = hypot(op, adj)
print('O comprimento da hipotenusa é: {:.2f} '.format(comp))

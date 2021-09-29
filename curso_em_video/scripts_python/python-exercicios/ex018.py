# Exercicio 018 do curso de Python - Curso em vídeo

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# Seno, Cosseno e tangente desse ângulo.

from math import radians, cos, sin, tan
ang = int(input('Digite o ângulo: '))
print('Para o ângulo de: {}\nO valor do seno é: {:.2f}, cosseno é: {:.2f} e tangente é: {:.2f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))

# Correção - Ok
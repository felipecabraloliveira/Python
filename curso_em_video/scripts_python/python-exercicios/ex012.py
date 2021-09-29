# Exercicio 012 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia o preço de um produto e mostre o seu novo preço,
# com 5% de desconto.

p = float(input('Digite o preço do produto: R$ '))

print('O produto custa R$ {:.2f} e com desconto de 5% sai por R${:.2f}'.format(p,p - (p/100*5)))

# Correção - OK
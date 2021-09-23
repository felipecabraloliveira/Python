# Exercicio 011 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia a largura e altura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2m quadrados

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))

print('Para uma parede de {:.2f} de largura e {:.2f} de altura no total {:.2f} m2, é necessário {:.2f}l de tinta para pintá-la.'.format(l,a, a*l ,(a*l)/2))

# Correção - OK
# Exercicio 022 do curso de Python - Curso em vídeo

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras Maiúsculas
# 2. O nome com todas as letras Minúsculas
# 3. Quantas letras ao (todo sem considerar os espaços)
# 4. Quantas letras tem o primeiro nome

# Meu código
nome = str(input('Digite o seu nome completo: '))
print('Nome com letras Maiúsculas: {}'.format(nome.upper()))
print('Nome com letras Minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras s/espaços: {} ' .format(len(nome.replace(' ', ''))))
print('Quantidade de letras c/espaços: {}' .format(len(nome)))
lista = nome.split()
print('O primeiro nome possui {} letras.'.format(len(lista[1])))

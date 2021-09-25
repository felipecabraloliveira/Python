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
print('O seu primeiro nome {} possui {} letras.'.format(lista[0], len(lista[0])))

# Correção - OK

print('\n\nOutras formas de atingir os resultados!')
nome = str(input('Digite o seu nome completo: ')).strip() # remover os espaços na captação do teclado
print('Quantidade de letras s/espaços: {} ' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) # vai encontrar a primeira posiçaõ vazia, mostrando a quantidade de letras.

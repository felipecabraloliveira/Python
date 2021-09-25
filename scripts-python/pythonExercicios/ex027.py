# Exercicio 027 do curso de Python - Curso em vídeo

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
# Ex. Ana Maria de Souza
# Saida - Primeiro: ANA - último: Souza

nome = str(input('Digite o nome completo:'))
nome = nome.strip()
lista = nome.split()
pos = nome.rfind(' ')
print('Nome digitado: {}\nPrimeiro: {}\n Último: {}'.format(nome, lista[0], nome[pos:]))

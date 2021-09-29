# Exercicio 027 do curso de Python - Curso em vídeo

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
# Ex. Ana Maria de Souza
# Saida - Primeiro: ANA - último: Souza

nome = str(input('Digite o nome completo: ')).strip()
nome = nome.strip()
lista = nome.split()
pos = nome.rfind(' ')
print('Nome digitado: {}\nPrimeiro: {}\n Último: {}'.format(nome, lista[0], nome[pos:]))

# Correção - Ajustar a posição do caracter exibido.

print('\n\n***Outra forma de atingir os resultados!***')
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))

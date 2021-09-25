# Exercicio 025 do curso de Python - Curso em vídeo

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA no nome.

nome = str(input('Digite o seu nome completo: ')).strip() # Removendo os espaços
print("Você possui o sobrenome SILVA: {}".format('SILVA' in nome.upper()))

# Correção
print('\n\n***Outra forma de atingir os resultados!***')
nome = str(input('Digite o seu nome completo: ')).strip() # Removendo os espaços
print('Seu nome tem silva? {}'.format('silva' in nome.lower()))

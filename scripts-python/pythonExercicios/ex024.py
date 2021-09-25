# Exercicio 024 do curso de Python - Curso em vídeo

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da Cidade: '))
lista = cidade.split()
print('A cidade começa com SANTO: {}'.format('SANTO' in lista[0]))

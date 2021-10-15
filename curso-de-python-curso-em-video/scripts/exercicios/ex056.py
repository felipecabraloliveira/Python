# Exercício 056 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 32)
print(' ' * 6 + 'Analisador Completo!')
print('*' * 32)
maior = 0
menor = 0
nome = ''
idade = ''
sexo = ''
for c in range(1, 3):
    nome[] += str(input('Digite o nome da pessoa {}: '.format(c)))
    idade += str(input('Digite a Idade da pessoa {}: '.format(c)))
    sexo += str(input('Digite o Sexo da pessoa {}: '.format(c)))
    print('\n')

nome = nome.split()
idade = idade.strip()
sexo = sexo.strip()
print(nome[0])
print(idade[0])
print(sexo[0])

# Continuar....
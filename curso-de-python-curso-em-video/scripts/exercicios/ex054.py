# Exercício 054 do curso de Python - Curso em vídeo

# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

# Meu Código
from datetime import date
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 32)
print(' ' * 6 + 'Grupo da Maioridade!')
print('*' * 32)
y = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    if y - ano < 18:
        menor += 1
    else:
        maior += 1
print('{}{}{} pessoas ainda não atingiram a maioridade e {}{}{} já são maiores de idade!'
      .format(cores['g'], menor, cores['remove'], cores['red'], maior, cores['remove']))

# Exercício 055 do curso de Python - Curso em vídeo

# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

# Meu Código
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 32)
print(' ' * 6 + 'Maior e Menor peso!')
print('*' * 32)
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da pessoa {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}Kg\n'
      'O menor peso é {}Kg'.format(maior, menor))
# Correção - OK
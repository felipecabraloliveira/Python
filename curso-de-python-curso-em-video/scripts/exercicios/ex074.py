# Exercício 074 do curso de Python - Curso em vídeo

#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
#  valor que estão na tupla.

# Meu Código
print('=' * 37)
print(' ' * 5 + 'Maior e Menor Valor!')
print('=' * 37)

from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Sorteado o valor {}'.format(n))
print('Os valores sorteados foram: ')
for c in n:
    print(f'{c} ', end='')
print(f'\nO Maior valor sorteado foi {max(n)}')
print(f'O Menor valor sorteado foi {min(n)}')

# Correção - Ok


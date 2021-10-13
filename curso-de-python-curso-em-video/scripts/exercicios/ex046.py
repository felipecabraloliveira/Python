# Exercício 046 do curso de Python - Curso em vídeo

# Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

# Meu Código
from time import sleep
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m',
         'vmc': '\033[1;91m', 'vc': '\033[1;92m', 'ac': '\033[1;93m',  'remove': '\033[0;0m'}
print('*' * 32)
print(' ' * 6 + 'Contagem Regressiva!')
print('*' * 32)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('{}FOGOS!!!{}'.format(cores['red'], cores['remove']))
# Correção - Ok

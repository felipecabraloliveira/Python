# Exercício 047 do curso de Python - Curso em vídeo

# Crie um programa que mostre na tela todos os números pares que
# estão no intervalo entre 1 e 50.

# Meu Código
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m',
         'vmc': '\033[1;91m', 'vc': '\033[1;92m', 'ac': '\033[1;93m',  'remove': '\033[0;0m'}
print('*' * 26)
print(' ' * 6 + 'Números Pares!')
print('*' * 26)
print('{}Imprimindo na tela números pares de 1 a 50!{}'.format(cores['blue'], cores['remove']))
for c in range(1, 51):
    if c % 2 == 0:
        print(c)

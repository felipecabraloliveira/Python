# Exercício 052 do curso de Python - Curso em vídeo

# Faça um programa que leia um número inteiro e diga se
# ele é ou não um número primo.

# Meu Código
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 32)
print(' ' * 6 + 'Números Primos!')
print('*' * 32)
num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('{}'.format(cores['g']), end ='')
        cont += 1
    else:
        print('{}'.format(cores['red']), end ='')
    print('{} '.format(c), end= '')
print('{}\nO número {} foi divisível {} vezes.'.format(cores['remove'],num , cont))
if cont == 2:
    print('Portando, é PRIMO!')
else:
    print('Portando, não é PRIMO!')
# Correção - OK

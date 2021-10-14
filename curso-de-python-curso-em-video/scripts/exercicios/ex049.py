# Exercício 049 do curso de Python - Curso em vídeo

# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

# Meu Código
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m',
         'vmc': '\033[1;91m', 'vc': '\033[1;92m', 'ac': '\033[1;93m',  'remove': '\033[0;0m'}
print('*' * 26)
print(' ' * 6 + 'Tabuada vs2.0!')
print('*' * 26)
n = int(input('Digite um número: '))
print('{}Tabuada do {}{}'.format(cores['red'], n, cores['remove']))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
# Correção - Ok

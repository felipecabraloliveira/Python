# Exercício 042 do curso de Python - Curso em vídeo

# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

# Meu Código
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 30)
print(' ' * 5 + 'Tipos de Triângulo!')
print('*' * 30)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.', end='')
    if r1 == r2 and r2 == r3:
        print('O triângulo formado é um EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado é um ESCALENO!')
    else:
        print('O triângulo formado é um ISÓSCELES')
else:
    print('Os segmentos não podem formar triângulo.')
# Correção - Ok

# Exercício 060 do curso de Python - Curso em vídeo

# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# Meu Código
print('*' * 29)
print(' ' * 6 + 'Fatorial!!!')
print('*' * 29)
num = int(input('Digit um número: '))
cont = num
fatorial = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))

# Correção - Ok
print('\nOutra forma de atingir o objetivo, de forma mais simples!')
from math import factorial
n = int(input('Digite o número: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

# FOR
print('\nUtilizando FOR')
num = int(input('Digit um número: '))
cont = num
fatorial = 1
for c in range(num, 0, -1):
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))

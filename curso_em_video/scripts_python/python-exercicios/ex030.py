# Exercício 030 do curso de Python - Curso em vídeo

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Meu Código
n = int(input('Digite um número: '))
if n % 2 == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))

# Correção - Ok

print('\nOutra forma de atingir o objetivo!\n')
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))

# Exercício 035 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.

r1 = int(input('Digite a reta 1: '))
r2 = int(input('Digite a reta 2: '))
r3 = int(input('Digite a reta 3: '))

if r2 % r3 < r1 < (r2 + r3):
    if r1 % r3 < r2 < (r1 + r3):
        if r1 % r2 < r3 < (r1 + r2):
            print('Com as retas {}, {} e {} é possível formar um triângulo'.format(r1, r2, r3))
        else:
            print('Com as retas {}, {} e {} não é possível formar um triângulo'.format(r1, r2, r3))
else:
    print('Com as retas {}, {} e {} não é possível formar um triângulo'.format(r1, r2, r3))


# Exercício 033 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia três números e mostre qual é o amior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        ma = n1
    else:
        ma = n3
else:
    if n2 > n3:
        ma = n2
    else:
        ma = n3
if n1 < n2:
    if n1 < n3:
        me = n1
    else:
        me = n3
else:
    if n2 <  n3:
        me = n2
    else:
        me = n3
print('O menor número digitado foi o {}'.format(me))
print('O maior número digitado foi o {}'.format(ma))

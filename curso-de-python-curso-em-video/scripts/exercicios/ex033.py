# Exercício 033 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia três números e mostre qual é o amior e qual é o menor.

# Meu Código
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

# Correção - Ok

print('\nOutra forma de atingir o objetivo!\n')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi o {}'.format(menor))
print('O maior valor digitado foi o {}'.format(maior))

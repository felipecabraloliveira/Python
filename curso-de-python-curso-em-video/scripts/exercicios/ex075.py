# Exercício 075 do curso de Python - Curso em vídeo

#  Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
#  em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Meu Código

print('=' * 37)
print(' ' * 5 + 'Análise de dados em Tupla!')
print('=' * 37)

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Os números digitados foram: {num}')

print(f'\nA - O valor 9 aparece: {num.count(9)} vez(es).')

if 3 in num:
    print(f'\nB - O número 3 apareceu na posição {num.index(3)+1} vezes.')
else:
    print('\nB - O valor 3 não foi digitado!')
print(f'\nC - Números pares: ', end='')

for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')


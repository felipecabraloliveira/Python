# Exercício 051 do curso de Python - Curso em vídeo

#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os 10 primeiros termos dessa progressão.

# Meu Código
print('*' * 32)
print(' ' * 6 + '10 Termos de uma PA!')
print('*' * 32)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(pri, razao * 10 , razao):
    print(c, end= ' ')
    print('->', end= ' ')
print('Acabou!')
# Correção - Ok
# Utilizar matematica para resolver.
dec = pri + (10 - 1) * razao
for c in range(pri, dec + razao, razao):
    print(c, end= ' ')
    print('->', end= ' ')
print('Acabou!')

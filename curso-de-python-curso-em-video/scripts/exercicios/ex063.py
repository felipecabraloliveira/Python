# Exercício 063 do curso de Python - Curso em vídeo

#  Escreva um programa que leia um número N inteiro qualquer e mostre
#  na tela os N primeiros elementos de uma Sequência de Fibonacci

# Meu Código
print('*' * 33)
print(' ' * 5 + 'Sequência de Fibonacci!')
print('*' * 33)
elemento = int(input('Digite quantos termos você quer que mostre: '))
cont = 3
ant = 0
atu = 1
print('{} - {}'.format(ant, atu), end='')
while cont <= elemento:
    prox = ant + atu
    print(' - {}'.format(prox), end='')
    ant = atu
    atu = prox
    cont += 1
print(' -> Pausa')
# Correção - Ok

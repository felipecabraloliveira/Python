# Exercício 045 do curso de Python - Curso em vídeo
# Crie um programa que faça o computador jogar Jokenpô com você.
import random as r
from time import sleep

# Meu Código
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 32)
print(' ' * 2 + 'GAME: Pedra Papel e Tesoura!')
print('*' * 32)
print('Suas opções:')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
jogada = int(input('Qual é a sua jogada? '))
comp = r.randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(1)
print('PO!!!')
if jogada == 0 and comp == 1:
    print('Vitória do Computador!!!')
    djogada = 'Pedra'
    dcomp = 'Papel'
elif jogada == 0 and comp == 2:
    print('Você venceu!!!')
    djogada = 'Pedra'
    dcomp = 'Tesoura'
elif jogada == 1 and comp == 0:
    print('Você venceu!!!')
    djogada = 'Papel'
    dcomp = 'Pedra'
elif jogada == 1 and comp == 2:
    print('Vitória do Computador!!!')
    djogada = 'Papel'
    dcomp = 'Tesoura'
elif jogada == 2 and comp == 0:
    print('Vitória do Computador!!!')
    djogada = 'Tesoura'
    dcomp = 'Pedra'
elif jogada == 2 and comp == 1:
    print('Você venceu!!!')
    djogada = 'Tesoura'
    dcomp = 'Papel'
else:
    print('Empate!!!')
    dcomp = jogada
    djogada = jogada
print('Computador: {} x você: {}'.format(dcomp, djogada))

# Correção
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O computador escolheu{}'. format(computador))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'. format(itens[computador]))
print('Jogador jogou {}'. format(itens[jogador]))
print('-='*11)
if computador == 0: # Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('{}Opção inválida!{}'.format(cores['red'], cores['remove']))
elif computador == 1: # Papel
    if jogador == 0:
        print('Computador Vence!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence!')
    else:
        print('{}Opção inválida!{}'.format(cores['red'], cores['remove']))
elif computador == 2: # Tesoura
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Computador Vence!')
    elif jogador == 2:
        print('Empate')
    else:
        print('{}Opção inválida!{}'.format(cores['red'], cores['remove']))

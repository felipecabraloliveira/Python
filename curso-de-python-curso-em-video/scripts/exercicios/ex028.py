# Exercício 028 do curso de Python - Curso em vídeo

# Faça um programa que pense em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Meu Código
from random import randrange
n = int(input('Qual o número o computador pensou entre 0 e 5: '))
p = randrange(1,5)
if n == p:
    print('Parabéns você acertou o número pensado pelo computador! número: {}'.format(n))
else:
    print('Ahh! Que pena você errou, o número que o computador pensou foi o {}'.format(p))

# Correção
print('\n\nOutra forma de atingir o objetivo!!!\n')
from random import randint
from time import sleep
computador = randint(0,5) # Computador sorteia número entre 0 e 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if computador == jogador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador,jogador))

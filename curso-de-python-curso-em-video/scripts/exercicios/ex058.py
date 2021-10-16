# Exercício 058 do curso de Python - Curso em vídeo

# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('*' * 32)
print(' ' * 3 + 'Jogo de Adivinhação vs2.0')
print('*' * 32)
comp = randint(0, 10)
print('Tente adivinhar o número que o computador pensou entre 0 e 10!')
jogador = int(input('Qual a sua jogada? '))
tentativas = 1
while jogador != comp:
    jogador = int(input('Que pena você errou, tente novamente: '))
    tentativas += 1
print('Parabéns Você acertou!!! O número pensado foi o {} e você levou {} tentativas para acertar.'
      .format(comp, tentativas))

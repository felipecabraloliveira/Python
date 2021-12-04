# Exercício 068 do curso de Python - Curso em vídeo

# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de
# vitórias consecutivas que ele conquistou no final do jogo.

# Meu Código

from random import randint
print('*' * 37)
print(' ' * 8 + 'Jogo do Par ou ímpar')
print('*' * 37)
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tp = ' '
    while tp not in 'PI':
        tp = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, total de {total}.')
    if tp == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tp == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!! VOCÊ VENCEU {v} VEZES.')

# Correção -OK

# Exercício 088 do curso de Python - Curso em vídeo

#  Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#  O programa vai perguntar quantos jogos serão gerados e vai sortear
#  6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# Meu Código
from random import randint
from time import sleep
print('=' * 37)
print(' ' * 4 + 'Palpites para a Mega Sena')
print('=' * 37)

jogos = int(input('Quantos jogos você quer sortear? '))
lista = []
temp = []
num = 0
for c in range(0, jogos):
    for s in range(0, 6):
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
    lista.append(temp[:])
    temp.clear()

for c in range(0, jogos):
    lista[c].sort()
    print(f'Jogo N°{c+1}: {lista[c]}')
    sleep(1)

# Outra forma

print('\nOutra forma!')

combo = list()
jogo = []
quant = int(input('Quantos jogos você quer que eu sortei? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in combo:
            combo.append(numero)
            cont += 1
        if cont >= 6:
            break
    combo.sort()
    jogo.append(combo[:])
    combo.clear()
    tot += 1
print('=' * 3, f'Sorteando {quant} Jogos', '=' * 3)
for i, l in enumerate(jogo):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=' * 7, 'Boa sorte!', '=' * 7)
# Correção - OK

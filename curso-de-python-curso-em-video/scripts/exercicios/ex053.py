# Exercício 053 do curso de Python - Curso em vídeo

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
#
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# Meu Código
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 29)
print(' ' * 3 + 'Detector de Palíndromo!')
print('*' * 29)
frase = str(input('Escreva uma frase: ')).upper().strip()
tratamento = frase.replace(' ', '')
qtd = len(tratamento)
inverso = ''
cont = 0
for c in range(qtd-1, -1, -1):
    # print(c)
    inverso += tratamento[c]
if inverso == tratamento:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
print('Palavra {} x Inverso {}'.format(tratamento, inverso))
# Correção - Ok
# Outra forma de atingir o objetivo
tratamento = frase.split()
junto = ''.join(tratamento)
# Sem utilizar o for
inverso = junto[::-1]
print(inverso)

# Exercício 081 do curso de Python - Curso em vídeo

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Extraindo dados de uma Lista')
print('=' * 37)
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
qt = 0
cont = ''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    qt += 1
    if cont == 'N':
        break
print('=' * 30)
print(f'Foram digitados {qt} número(s).')
valores.sort(reverse=True)
print(f'Lista em ordem decrescente: {valores}')
if 5 in valores:
    print(f'O valor 5 {cores["blue"]}consta{cores["remove"]} na lista!')
else:
    print('O valor 5 {}Não consta{} na lista!'.format(cores['red'], cores['remove']))

# Outra forma de verificar a quantidade de valores na lista:
print(f'\nOutra forma: '
      f'\nQuantidade de valores digitados na lista: {len(valores)}')
# Correção - OK

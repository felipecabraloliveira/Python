# Exercício 032 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia um ano qualquer e mostre se ele é BISSEXTO

# Meu Código
a = int(input('Digite o ano: '))
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('O ano {} é BISSEXTO.'.format(a))
        else:
            print('O ano {} não é BISSEXTO.'.format(a))
    else:
        print('O ano {} é BISSEXTO.'.format(a))
else:
    print('O ano {} não é BISSEXTO.'.format(a))

# Correção - Código da correção mais simples e limpo.

print('\nOutra forma de atingir o objetivo!\n')
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))

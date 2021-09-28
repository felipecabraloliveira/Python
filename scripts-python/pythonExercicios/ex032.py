# Exercício 032 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia um ano qualquer e mostre se ele é BISSEXTO

a = int(input('Digite o ano: '))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('O ano {} é BISSEXTO.'.format(a))
    else:
        print('O ano {} é BISSEXTO.'.format(a))
else:
    print('O ano {} não é BISSEXTO.'.format(a))
# Exercício 056 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 32)
print(' ' * 6 + 'Analisador Completo!')
print('*' * 32)
vnome = ''
vidade = 0
media = 0
m20 = 0
for c in range(1, 5):
    print('{}° Pessoa'.format(c))
    nome = str(input('Digite o nome: ')).strip().upper()
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Digite o Sexo [F/M]: ')).strip().upper()
    media += idade
    if sexo == 'M':
        if idade > vidade:
            vnome = nome
            vidade = idade
    else:
        if idade < 20:
            m20 += 1
    print('*-' * 16)
print('Média de idade:  {} anos'.format(media / 4))
print('Homem mais velho:  {} com {} anos'.format(vnome, vidade))
print('Mulheres com menos de 20 anos: {}'.format(m20))
# Correção - OK

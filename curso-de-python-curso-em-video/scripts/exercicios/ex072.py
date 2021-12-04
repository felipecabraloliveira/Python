# Exercício 072 do curso de Python - Curso em vídeo

# 72: Crie um programa que tenha uma dupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um número
# pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Meu Código
print('=' * 37)
print(' ' * 9 + 'Número por Extenso!')
print('=' * 37)

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
            'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
cont = ' '
# Evitando que o número digitado esteja fora do range
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {contagem[num]}')
        cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    else:
        print('Número incorreto, tente novamente. ', end='')
    if cont == 'N':
        break

# Outra forma de chegar oo resultado
print('\nOutro método!')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {contagem[num]}')

# Correção - Ok

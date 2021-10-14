# Exercício 050 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Meu Código
print('*' * 41)
print(' ' * 6 + 'Soma números pares digitados!')
print('*' * 41)
soma = 0
cont = 0  # Add na correção
for c in range(1, 7):
    n = int(input('Digite o número {}: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números pares e a soma deles é {}'.format(cont, soma))
# Correção - Ok

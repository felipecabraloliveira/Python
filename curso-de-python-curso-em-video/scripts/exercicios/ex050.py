# Exercício 050 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Meu Código
soma = 0
for c in range(1, 7):
    n = int(input('Digite o número {}: '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares digitados é {}'.format(soma))

# Exercício 066 do curso de Python - Curso em vídeo

# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma
# entre elas (desconsiderando o flag).

# Meu Código
print('*' * 37)
print(' ' * 4 + 'Números Inteiros')
print('*' * 37)

num = soma = cont = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num

print('Foram digitados {} números e a soma deles é {}.'.format(cont, soma))
# Correção OK

# Exercício 064 do curso de Python - Curso em vídeo

# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

# Meu Código
print('*' * 33)
print(' ' * 5 + 'Tratando vários valores vs1.0')
print('*' * 33)
cont = soma = num = 0
while num != 999:
    num = int(input('Digite um número ou [999 para sair]: '))
    if num != 999:
        soma += num
        cont += 1
print('A soma dos números é {} e foi digitado {} números!'.format(soma, cont))

# Exercício 065 do curso de Python - Curso em vídeo

# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

# Meu Código
print('*' * 37)
print(' ' * 4 + 'Maior e menor valores vs1.0')
print('*' * 37)
soma = cont = nummaior = nummenor = 0
continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        nummaior = nummenor = num
    else:
        if nummaior < num:
            nummaior = num
        if nummenor > num:
            nummenor = num
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('A média dos {} números digitados é {:.2f}'.format(cont, soma / cont))
print('O maior número foi o {} e o menor foi o {}'.format(nummaior, nummenor))
# Correção - OK

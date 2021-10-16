# Exercício 060 do curso de Python - Curso em vídeo

# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# Meu Código
print('*' * 29)
print(' ' * 6 + 'Fatorial!!!')
print('*' * 29)
num = int(input('Digit um número: '))
cont = 1
conta = 0
fatorial = num
while cont < num - 1:
    conta = fatorial * (num - cont)
    fatorial = conta
    cont += 1
print('O fatorial de {}! é igual a {}'.format(num, fatorial))

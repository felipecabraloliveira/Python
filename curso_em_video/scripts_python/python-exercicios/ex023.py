# Exercicio 023 do curso de Python - Curso em vídeo

# Crie um programa que leia um número de 0 a 9999 emostre na tela cada um dos digitos separados.

# Meu Código
print('Realizando tarefa com String! Depende que o número digitado possua 4 casas')
num = str(input('Digite um número entre 0 e 9999: '))
print('Número digitado: {}\nUnidade:{}\nDezena:{}\nCentena:{}\nMilhar:{}'.format(num, num[3], num[2], num[1], num[0]))

print('\nRealizando tarefa com Números Int!')
num1 = int(input('Digite um número entre 0 e 9999: '))
print('Número digitado: {}\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num1, num1 % 1000 % 100 % 10, num1 % 1000 % 100 // 10, num1 % 1000 // 100, num1 // 1000))

# Correção
print('\n\n***Outra forma de atingir os resultados!***')

u = num1 // 1 % 10
d = num1 // 10 % 10
c = num1 // 100 % 10
m = num1 // 100 % 100

print('Analisando o número: {}'.format(num1))
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(u))
print('Milhar:  {}'.format(m))

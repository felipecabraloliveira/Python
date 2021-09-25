# Exercicio 023 do curso de Python - Curso em vídeo

# Crie um programa que leia um número de 0 a 9999 emostre na tela cada um dos digitos separados.

# Meu Código
print('Realizando tarefa com String!')
num = str(input('Digite um número entre 0 e 9999: '))
print('Número digitado: {}\nUnidade: {}\nDezena:{}\nCentena: {}\nMilhar: {}'  .format(num, num[3], num[2], num[1], num[0]))

print('Realizando tarefa com Números Int!')
num1 = int(input('Digite um número entre 0 e 9999: '))
print('Número digitado: {}\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num1, num1 % 1000 % 100 % 10, num1 % 1000 % 100 // 10, num1 % 1000 // 100, num1 // 1000))

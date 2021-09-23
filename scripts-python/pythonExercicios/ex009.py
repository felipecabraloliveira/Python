# Exercicio 009 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

# meu código apenas com o aprendizado até o momento
n = int(input('Digite um número inteiro: '))
print('Tabuada do {}:'.format(n))
print('{} x 1: {}\n{} x 2: {}\n{} x 3: {}\n{} x 4: {}\n{} x 5: {}\n{} x 6: {}\n{} x 7: {}\n{} x 8: {}\n{} x 9: {}\n{} x 10: {}'.format(n,n*1,n,n*2,n,n*3,n,n*4,n,n*5,n,n*6,n,n*7,n,n*8,n,n*9,n,n*10))


# meu código utilizando laço de repetição While
n = int(input('Digite um número inteiro: '))
i = 1
print('Tabuada do {}:'.format(n))
while(i <= 10):
    print('{} x {}: {}'.format(n,i,n*i))
    i = i+1

# Correção - OK
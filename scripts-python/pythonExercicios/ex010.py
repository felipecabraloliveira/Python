# Exercicio 010 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar. $3,27

n = float(input('Digite quanto você tem em sua carteira: R$ '))
print('Você possui R$ {} e pode comprar ${:.3} Dólares.'.format(n, n / 3.27))

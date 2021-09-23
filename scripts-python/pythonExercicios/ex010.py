# Exercicio 010 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar. $3,27
# Dólar Hoje 5,30 - 23/09/2021

valor = float(input('Digite quanto você tem em sua carteira: R$ '))
cotacao = float(input('Digite a cotação do Dólar: $ '))
print('Você possui R${:.2f} e pode comprar ${:.2f} Dólares.'.format(valor, valor / cotacao))

# Resultado:

# Digite quanto você tem em sua carteira: R$ 12.35
# Digite a cotação do Dólar: $ 5.30
# Você possui R$ 12.35 e pode comprar $2.33 Dólares.

# Correção - OK
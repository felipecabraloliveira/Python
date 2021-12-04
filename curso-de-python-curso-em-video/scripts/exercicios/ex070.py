# Exercício 070 do curso de Python - Curso em vídeo

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Meu Código
print('*' * 37)
print(' ' * 16 + 'Loja')
print('*' * 37)
total = totmil = menor = temp = 0
prodbarato = ' '
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    temp += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if temp == 1:
        menor = preco
        prodbarato = produto
    else:
        if preco < menor:
            menor = preco
            prodbarato = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Você quer Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print('-' * 37)
print(f'O Valor total da compra é R${total:.2f}')
print(f'Temos no total {totmil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato é o {prodbarato} custa R${menor:.2f}')

# Correção - Ok

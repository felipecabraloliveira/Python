# Exercício 076 do curso de Python - Curso em vídeo

#  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
#  na sequência. No final, mostre uma listagem de preços,
#  organizando os dados em forma tabular.

# Meu Código

print('=' * 37)
print(' ' * 5 + 'Lista de Preços com Tupla!')
print('=' * 37)

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('-' * 45)
print(' ' * 13 + 'Listagem de Preço!')
print('-' * 45)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R${produtos[c]:>7.2f}')
print('=' * 45)

# Correção- OK

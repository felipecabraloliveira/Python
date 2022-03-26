# Exercício 087 do curso de Python - Curso em vídeo

#  Aprimore o desafio anterior, mostrando no final:
#  A) A soma de todos os valores pares digitados.
#  B) A soma dos valores da terceira coluna.
#  C) O maior valor da segunda linha.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Mais sobre Matriz em Python')
print('=' * 37)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um Valor para a posição [{l}, {c}]: '))
par = soma = mvalor = 0
print('=' * 37)
for p in range(0, 3):
    for q in range(0, 3):
        print(f'[{matriz[p][q]:^5}]', end='')

        if matriz[p][q] % 2 == 0:
            par += matriz[p][q]
    print()
for c in range(0, 3):
    soma += matriz[c][2]

for c in range(0, 3):
    if c == 0:
        mvalor = matriz[1][c]
    elif matriz[1][c] > mvalor:
        mvalor = matriz[1][c]
print(f'\nA soma dos números pares é {par}.')
print(f'A soma da terceira coluna é {soma}.')
print(f'O maior valor da segunda Linha é {mvalor}.')

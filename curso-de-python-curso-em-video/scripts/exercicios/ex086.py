# Exercício 086 do curso de Python - Curso em vídeo

#  Crie um programa que declare uma matriz de dimensão 3×3 e
#  preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Matriz em Python')
print('=' * 37)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um Valor para a posição [{l}, {c}]: '))

print('=' * 37)
for p in range(0, 3):
    for q in range(0, 3):
        print(f'[{matriz[p][q]:^5}]', end='')
    print()

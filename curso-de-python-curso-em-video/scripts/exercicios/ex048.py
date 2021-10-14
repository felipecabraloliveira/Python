# Exercício 048 do curso de Python - Curso em vídeo

# Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

# Meu Código
print('*' * 54)
print(' ' * 6 + 'Números Ímpares e soma dos Múltiplos de 3!')
print('*' * 54)
soma = 0
cont = 0  # Add na correção
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores que são múltiplos de três de 1 a 500 foi {}'.format(cont, soma))
# Correção - Ok

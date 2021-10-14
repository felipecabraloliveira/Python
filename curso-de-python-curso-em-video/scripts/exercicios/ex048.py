# Exercício 048 do curso de Python - Curso em vídeo

# Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

# Meu Código
soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma entre os multiplos de três de 1 a 500 foi {}'.format(soma))

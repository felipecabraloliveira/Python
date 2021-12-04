# Exercício 072 do curso de Python - Curso em vídeo

# 72: Crie um programa que tenha uma dupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um número
# pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Meu Código
print('=' * 37)
print(' ' * 9 + 'Número por Extenso!')
print('=' * 37)

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
            'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = -1
# Evitando que o número digitado esteja fora do range
while num < 0 or num > 20:
    num = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {contagem[num]}')

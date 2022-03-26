# Exercício 078 do curso de Python - Curso em vídeo

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

print('=' * 37)
print(' ' * 8 + 'Lista - Maior e Menor')
print('=' * 37)

valores = []
menor = 9999999
maior = 0

for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

for c, v in enumerate(valores):
    if(v <= menor):
        menor = v
    if(v >= maior):
        maior = v

print(f'\nVocê digitou os valores {valores}')
for c, v in enumerate(valores):

    if(v == maior):
        print(f'\nO menor valor da lista foi {maior} na posição {c}')
    if (v == menor):
        print(f'\nO menor valor da lista foi {menor} na posição {c}')

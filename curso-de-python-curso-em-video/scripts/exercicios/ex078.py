# Exercício 078 do curso de Python - Curso em vídeo

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

print('=' * 37)
print(' ' * 8 + 'Lista - Maior e Menor')
print('=' * 37)

valores = []
menor = 0
maior = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'\nVocê digitou os valores {valores}')
print(f'O Maior valor da lista foi {maior} nas posições: ',end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'\nO Menor valor da lista foi {menor} nas posições: ',end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end='')
# Correção - OK
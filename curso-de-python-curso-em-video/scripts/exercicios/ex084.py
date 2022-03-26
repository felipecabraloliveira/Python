# Exercício 084 do curso de Python - Curso em vídeo

#  Faça um programa que leia nome e peso de várias pessoas,
#  guardando tudo em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
#  C) Uma listagem com as pessoas mais leves.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Lista composta e análise de dados')
print('=' * 37)
pessoa = list()
dadotemp = list()
maior = menor = 0
while True:
    dadotemp.append(str(input('Nome: ')))
    dadotemp.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = dadotemp[1]
    else:
        if dadotemp[1] > maior:
            maior = dadotemp[1]
        if dadotemp[1] < menor:
            menor = dadotemp[1]
    pessoa.append(dadotemp[:])
    dadotemp.clear()
    cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print('=' * 37)
print(f'Lista Cadastrada: {pessoa}')
print(f'Quantidade de Pessoas cadastradas: {len(pessoa)}')
print(f'O maior peso foi de {maior}Kg, Peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'{p[0]}...', end='')
print()
print(f'O menor peso foi de {menor}Kg, Peso de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f'{p[0]}...', end='')
# Correçã - OK

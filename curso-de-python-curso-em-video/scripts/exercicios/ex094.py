# # Exercício 094 do curso de Python - Curso em vídeo

# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

print('=' * 37)
print(' ' * 5 + 'Unindo dicionários e listas')
print('=' * 37)

pessoa = dict()
lista = list()

while True:
    pessoa['Nome'] = str(input('Nome: ').title().strip())
    pessoa['Sexo'] = str(input('Sexo: ')).upper()
    while pessoa['Sexo'] not in 'FM':
        print('Valor incorreto! Esperado [M/F]')
        pessoa['Sexo'] = str(input('Sexo: ')).upper()
    pessoa['Idade'] = int(input('Idade: '))
    cont = str(input('Deseja continuar? [S/N]')).upper()
    while cont not in 'SN':
        print('Valor incorreto! Esperado [S/N]')
        cont = str(input('Deseja continuar? [S/N]')).upper()
    lista.append(pessoa)
    if cont in 'N':
        break
print(lista)
# Continuar

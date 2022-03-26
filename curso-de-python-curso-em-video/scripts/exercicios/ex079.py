# Exercício 079 do curso de Python - Curso em vídeo

# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.

from time import sleep
print('=' * 37)
print(' ' * 5 + 'Valores únicos em uma lista')
print('=' * 37)

cont = ''
valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('O valor digitado já existe, tente outro...')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print('-=' * 30)
print('Analisando os dados...')
sleep(2)
print(f'\nOs valores digitados foram: {valores}')
valores.sort()
print(f'Colocando a lista em ordem crescente: {valores}')
#Correção - OK

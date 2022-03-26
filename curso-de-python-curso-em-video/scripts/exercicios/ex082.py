# Exercício 082 do curso de Python - Curso em vídeo

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Dividindo valores em várias listas')
print('=' * 37)

cont = ''
valores = []
vpar = []
vimpar = []
while True:
    num = int(input('Digite um valor: '))
    cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if num % 2 == 0:
        vpar.append(num)
    else:
        vimpar.append(num)
    valores.append(num)
    if cont == 'N':
        break
print('=' * 37)
print(f'Lista completa: {valores}')
print(f'Lista de números Pares: {vpar}')
print(f'Lista de números Ímpares: {vimpar}')

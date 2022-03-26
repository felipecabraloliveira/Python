# Exercício 085 do curso de Python - Curso em vídeo

#  Crie um programa onde o usuário possa digitar sete valores numéricos
#  e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Listas com pares e ímpares')
print('=' * 37)

principal = list()
par = list()
impar = list()
for pos in range(0, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
principal.append(par[:])
principal.append(impar[:])
print('=' * 37)

print(f'Valores Pares: {principal[0]}')
print(f'Valores Ímpares: {principal[1]}')
principal[0].sort()
principal[1].sort()
print(f'Lista ordenada: {principal}')

# Outra forma:
print('\nOutra forma:')
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os valores: {num}')
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
# Correção - Ok

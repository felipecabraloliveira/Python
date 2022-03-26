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

print(f'Lista digitada: {principal}')
print(f'Valores Pares: {principal[0]}')
print(f'Valores Ímpares: {principal[1]}')
principal[0].sort()
principal[1].sort()
print(f'Lista ordenada: {principal}')

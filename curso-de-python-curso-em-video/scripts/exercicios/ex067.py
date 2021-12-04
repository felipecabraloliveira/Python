# Exercício 067 do curso de Python - Curso em vídeo

# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o
# número solicitado for negativo.

# Meu Código
print('*' * 37)
print(' ' * 11 + 'Tabuada Vs3.0')
print('*' * 37)

while True:
    n = int(input('Qual tabuada você quer? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('*' * 30)
# Correção - Ok

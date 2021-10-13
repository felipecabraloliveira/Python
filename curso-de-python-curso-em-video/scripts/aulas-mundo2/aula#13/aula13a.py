for c in range(1, 7):
    print(c)
print('Fim')
print('\n\n')
for c in range(6, 0, -1):
    print(c)
print('Fim')


n = int(input('Digite um número? '))
for c in range(0, n):
    print(c)
print('Fim!')

print('-' *20)
print('-' *20)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

print('-' *20)
print('-' *20)
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores é {}'.format(s))

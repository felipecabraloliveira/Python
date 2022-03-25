# Aula 17 do Curso de Python do Curso em Vídeo.

# Recapitulando tuplas que são imutáveis.
lanche = ('Hamburguer','Suco','Pizza')

print(lanche)

print('\n Listas!')
num = [2, 5, 9, 1]
num[2] = 3
print('\n', num)

# num[4] = 7  Não é possóvel adcionar elementos dessa forma, utilizar append
num.append(14)
print('\n', num)

print('\n#Ordenando a lista')
# Colocando em ordem
num.sort()
print('\n', num)

print('\n#Inserindo valores')
num.insert(2, 0) # Na posição dois inserir o valor 0.
print(num)
print(f'Essa lista tem {len(num)} elementos.')

print('\n#Removendo Valores')
# num.pop()  Elimina o último valor.
num.pop(2) # Elimina o valor do índice 2
print(num)

print('\n#Inserindo o valor 2 ao índice 2')
num.insert(2, 2)
print(num)

print('\n#Removendo o valor 2 da lista, \nlembrando que apenas o primeiro valor encontrado é removido.')
num.remove(2) #Elimina sempre o primeiro valor encontrado.
print(num)

print('\n#Laço para remover o valor 5 da lista.')
if 5 in num:
    num.remove(5)
    print('O número 5 foi removido da lista!')
else:
    print('Não foi encontrado o número 5 na lista')
print(num)

print('\nNova Lista!')
valores = list() # Criando uma lista vázia.
valores = [] # outra forma de criar lista vázia.

valores.append(5)
valores.append(9)
valores.append(4)

print('\nLista criada: ',valores)

print('\nExibindo a lista formatada: ', end='')
for v in valores:
    print(f'{v}...', end='')
print('\n')

print('\n#Inserindo via teclado valores na lista.')
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print('\n#Laço - Exibindo posição e valor.')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor: {v}')
print('Final da lista!')

print('\nNova lista')
a = [2, 3, 4, 7]
b = a

print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('\nAlterando a lista B, Posição 2 recebe o valor 8. '
      '\nPodemos verificar que a Lista A foi alterada também,'
      '\npois foi feito uma ligação entre as listas!')
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('\nCriando uma cópia de uma lista sem ligação.')
c = [2, 3, 4, 7]
d = a[:] # Cria uma cópia de C em D, mas sem Ligação.
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}')

# Aula 16 do Curso de Python do Curso em Vídeo.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[1])
print('\n\n')
# Tuplas são imutáveis

print(len(lanche))
print('\n\n')

for cont in range(0, len(lanche)):
    print(lanche[cont])
print('\n\n')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi bastante!')
print('\n\n')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('\n\n')

# Ordenando
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)

# Concatenando as duas Tuplas
c = a + b

print(c)
print(len(c))

# Conta quantas vezes o valor apareceu na tupla
print(c.count(5))
print(c.count(9))

# Mostra a posição que o valor aparece
print(c.index(5))
print('\n\n')

pessoa = ('Felipe', 27, 'M', 84.98)
print(pessoa)

# Apagando uma variável tupla
del(pessoa)
#print(pessoa)

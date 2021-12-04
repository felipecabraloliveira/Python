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
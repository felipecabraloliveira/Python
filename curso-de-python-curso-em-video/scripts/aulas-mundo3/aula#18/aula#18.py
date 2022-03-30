# Aula 17 do Curso de Python do Curso em Vídeo.

# Declarando um Dicionário:

pessoas = {'nome': 'Felipe', 'sexo': 'M', 'idade': 27}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')

# Print Values
print(f'Print Values: {pessoas.values()}')
# Print Keys
print(f'Print Keys(índices): {pessoas.keys()}')
# Print Items
print(f'Print Items: {pessoas.items()}')

# Utilizando laços em dicionários:
print('\nLaços em Dicionários!')

print('Laço com Keys')
for k in pessoas.keys():
    print(k)

print('\nLaço com Items')
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('\nApagando elementos do Dicionário! Ex. Sexo')
del pessoas['sexo']
print(pessoas)

print('\nAlterando e adicionando elementos ao Dicionário')
# Alterando o valor do elemento nome.
pessoas['nome'] = 'Leandro'
# Adicionando o elemento peso ao Dicionário.
pessoas['peso'] = 98.5
print(pessoas)

print('\nAdicionando um dicionário a uma lista!')
# Lista Brasil
brasil = []

# Dicionários
estado1 = {'uf': 'RJ', 'nome': 'Rio de Janeiro'}
estado2 = {'uf': 'SP', 'nome': 'São Paulo'}

# Adicionando os dicionários a lista.
brasil.append(estado1)
brasil.append(estado2)

print(f' Estado1 {estado1}')
print(f' Estado2 {estado2}')

print(f'\nLista Brasil: {brasil}')

print(f'\nLista Brasil posição 0: {brasil[0]}')
print(f'Lista Brasil posição 1: {brasil[1]}')

print(f'\nExibindo lista brasil posição 0 com elemento NOME: {brasil[0]["nome"]}')


print('\n')
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Nome do Estado: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for n in brasil:
    print(n)
    for k, v in n.items():
        print(f'O campo {k} tem valor {v}')

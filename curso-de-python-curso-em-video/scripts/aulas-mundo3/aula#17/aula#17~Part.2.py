# Aula 17 Parte 2 do Curso de Python do Curso em Vídeo

teste = list()
teste.append('Felipe')
teste.append(27)

print(teste)
print('\n')

galera = list()
galera.append(teste)
print(f'Exibindo lista Galera: {galera}')

teste[0] = 'Maria'
teste[1] = 40
galera.append(teste)
print(f'Exibindo lista Galera após alterar valores: {galera}')
print('Uma ligação criada, quando altera um, altera o outro'
      '\nportando nessa situação deve-se criar uma cópia.')

print('\nLista como cópia:')
galera1 = list()
teste1 = list()
teste1.append('Felipe')
teste1.append(27)

print('\n')
galera.append(teste[:])
teste1[0] = 'Maria'
teste1[1] = 40
galera1.append(teste[:])
print(f'Exibindo lista Galera após alterar valores: {galera1}')

print('\n')
pessoa = [['João', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]

print(f'Lista Pessoa -> {pessoa}')
print(f'pessoa[0]    -> {pessoa[0]}')
print(f'pessoa[0][0] -> {pessoa[0][0]}')
print(f'pessoa[0][1] -> {pessoa[0][1]}')
print('\n')
print(f'pessoa[2][1] -> {pessoa[2][1]}')

print('\nPrint Nomes e idade:')
for p in pessoa:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('\nCapturando o nome e idade do teclado:')
galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

totmai = totmen = 0
print('\nMostrando maiores e menores de idade!')
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

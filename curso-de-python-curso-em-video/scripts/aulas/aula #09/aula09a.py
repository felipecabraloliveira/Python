frase = 'Curso em Vídeo Python'
print(frase)
print('\nFatiando a String!')

print('\n\nRetornando apenas o valor armazenado na posição 3 da String! frase[3]')
print('Retorno: {}' .format(frase[3]))

print('\nRetornando da String a posição 3 até a 12! frase[3:13]')
print('Retorno: {}' .format(frase[3:13]))

print('\nRetornando do início da String até a posição 13! frase[:13]')
print('Retorno: {}' .format(frase[:13]))

print('\nRetornando da posição 13 da String até o final! frase[13:]')
print('Retorno: {}' .format(frase[13:]))

print('\nRetornando da posição 1 da String até a 14! frase[1:15]')
print('Retorno: {}' .format(frase[1:15]))

print('\nRetornando da posição 1 da String até a 14 e pulando de 2 em 2! frase[1:15:2]')
print('Retorno: {}' .format(frase[1:15:2]))

print('\nRetornando a quantidade de vezes que a letra o aperece na String! frase.count()')
print('Retorno: {}'.format(frase.count('o')))

print('\nRetornando a quantidade de vezes que a letra O maíusculo aperece na String! frase.count()')
print('Retorno: {}'.format(frase.count('O')))

print('\nRetornando a frase da String com letras maiúsculas! frase.upper()')
print('Retorno: {}'.format(frase.upper()))

print('\nRetornando a frase da String com letras minúsculas! frase.lower()')
print('Retorno: {}'.format(frase.lower()))

print('\nRetornando a quantidade de caracteres que a String possui! len(frase)')
print('Retorno: {}'.format(len(frase)))

print('\n***Alterando a String para que ela possua espaços em branco no começo e no final da String!***')

frase = '     Curso em Vídeo Python     '
print('\nRemovendo os espaços no começo e no final da String! frase.strip()')
print('Retorno: {}'.format(frase.strip()))
frase = frase.strip()

print('\nTrocando um conjunto de caracteres por outro dentro da String! frase.replace()')
print('Retorno: {}'.format(frase.replace('Python', 'Android')))

print('\nVerificando se uma palavra está dentro da String! ')
print('Retorno: {}'.format('Curso' in frase))

print('\nBuscando se uma palavra está dentro da String e retornando a posição que ela inicia! frase.find()')
print('Retorno: {}'.format(frase.find('Vídeo')))
print('Retorno caso não exista a palavra. Ex. php: {}'.format(frase.find('php')))

print('\nDividindo a String em listas, utilizando como base o espço para separar as palavras! frase.split()')
print('Retorno: {}'.format(frase.split()))

print('\nApós separar a String em uma lista e armazenar na variável dividido, podemos retornar apenas a palavra!desejada! dividido[3] ')
dividido = frase.split()
print('Lista {}'.format(dividido))
print('Retorno dividido[0]: {}' .format(dividido[0]))
print('Retorno dividido[1]: {}' .format(dividido[1]))
print('Retorno dividido[2]: {}' .format(dividido[2]))
print('Retorno dividido[3]: {}' .format(dividido[3]))

print('\nRetornando a posição do caracter de uma palavra de nossa lista! dividido[2][1]')
print('Retorno da palavra {} o valor da posição 1:  {}'.format(dividido[2], dividido[2][1]))

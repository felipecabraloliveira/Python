# Maneiras de importar a biblioteca math
import math                         # Importando todas as funcionalidades
from math import sqrt, ceil         # Importando duas funcionalidade específicas

num = int(input('Digite um número: '))

raiz = math.sqrt(num)   # Utilizar math.método para importação completa
raiz1 = sqrt(num)       # Utilizar apenas o método quando a importação for específica

print('A raiz de {} é igual a {}'.format(num,raiz))

# Resultado: A raiz de 29 é igual a 5.385164807134504

print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))

# Resultado: A raiz de 29 é igual a 6 - Arredondamento para cima
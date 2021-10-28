# Aula 15 do Curso de Python do Curso em Vídeo.

cont = 1
while cont <= 10:
    print(cont, '...', end='')
    cont += 1
print('Acabou')


n = s = 0
while n != 999:
    n = int(input('Digite um número: [parar 999] '))
    s += n
print('A som vale {}'.format(s))

# Problema do código anterior, é que o 999 que é apenas para controle entra na conta
# Resolvemos com a interrupção do While
soma = 0
while True:
    n = int(input('Digite um número: [parar 999]: '))
    if n == 999:
        break
    soma += n
# print('A som vale {}'.format(soma))

# utilizando as fstrings do Python.
print(f'A soma vale {soma}')

nome = 'Jose'
idade = 33

print(f'O {nome} tem {idade} anos!')  # Python 3.6
print('O {} tem {} anos!'.format(nome, idade))  # Python 3
print('O %s tem %d anos!' % (nome, idade))  # Python 2

salario = 987.35

print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')

# Centralizando o nome
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')

# Centralizando o nome com -
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')

# Alinhado a direita o nome com -
print(f'O {nome:->20} tem {idade} anos e ganha R${salario:.2f}')

# Alinhado a esquerda o nome com -
print(f'O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}')

# Alinhando a escrita em 20 caracteres
print(f'O {nome:20} tem {idade} anos e ganha R${salario:.2f}')

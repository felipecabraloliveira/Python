# Exercício 049 do curso de Python - Curso em vídeo

# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

# Meu Código
print('*' * 26)
print(' ' * 6 + 'Tabuada vs2.0!')
print('*' * 26)
n = int(input('Digite um número: '))
print('A tabuada do {}:'.format(n))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))

# Aula #11 - Trabalhando com cores no Python

print('\033[4;30;45mOlá, mundo!\033[m')

# Invertendo as cores:
print('\n\033[7;30;45mOlá, mundo!\033[m')

# texto sublinhado
print('\n\033[4;36;40mOlá, mundo!\033[m')

# texto Negrito
print('\n\033[1;97;40mOlá, mundo!\033[m')

print('\nExibindo números: ')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

print('\nExibindo nome na cor azul!')
nome = 'Felipe'
# Outra forma de adicionar formatação aos textos.
print('Olá! Seja bem-vindo {}{}{}, prazer em te conhecer!'.format('\033[1;94m', nome, '\033[m'))

print('\nCriando variáveis para facilitar o tratamento das cores!')

cores = {'remove':'\033[m', 'branco':'\033[1;97m', 'azul':'\033[1;34m', 'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['remove']))

# Exercício 057 do curso de Python - Curso em vídeo

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 32)
print(' ' * 6 + 'Validação de Dados!')
print('*' * 32)
sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite novamente o sexo [M/F]: ')).upper().strip()[0]
cor = '\033[1;35m'
if sexo == 'M':
    cor = '\033[1;34m'
print('{}Você selecionou o sexo {}{}' .format(cor, sexo, cores['remove']))
# Correção - Ok
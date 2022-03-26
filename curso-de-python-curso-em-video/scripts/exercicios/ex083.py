# Exercício 083 do curso de Python - Curso em vídeo

# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os
# parênteses abertos e fechados na ordem correta.
# Meu Código
print('=' * 37)
print(' ' * 4 + 'Validando expressões matemáticas')
print('=' * 37)
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
aberto = 0
fechado = 0
exp = str(input('Digite a expressão: ')).strip()
for v in exp:
    if v == '(':
        aberto += 1
    elif v == ')':
        fechado += 1
print('=' * 37)
if aberto == fechado:
    print(f'A expressão é {cores["blue"]}Válida!{cores["remove"]}')
else:
    print(f'A expressão está {cores["red"]}Incorreta!{cores["remove"]}')
print(f'Expressão: {exp}')

# Outra forma:
print("\nOutra forma:")
expr = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão não é válida!')

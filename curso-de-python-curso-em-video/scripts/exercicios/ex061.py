# Exercício 061 do curso de Python - Curso em vídeo

# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

# Meu Código
print('*' * 32)
print(' ' * 3 + 'Progressão Aritmética v2.0')
print('*' * 32)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec = pri + (10 - 1) * razao
cont = razao
while pri < dec + razao:
    print(pri, end=' ')
    print('->', end=' ')
    pri += razao
print('Acabou!')
# Correção - OK

print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro

cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')

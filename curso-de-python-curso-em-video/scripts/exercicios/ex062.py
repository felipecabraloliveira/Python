# Exercício 062 do curso de Python - Curso em vídeo

#  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.

# Meu Código
print('*' * 32)
print(' ' * 3 + 'Progressão Aritmética v3.0')
print('*' * 32)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = pri
cont = 1
mais = 10
vezes = 0
while mais != 0:
    vezes = vezes + mais
    while cont <= vezes:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('\nQuantos termos você quer mostrar a mais: '))
print('A progressão foi finalizada com {} termos exibidos.'.format(vezes))

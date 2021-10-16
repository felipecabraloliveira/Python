# Exercício 059 do curso de Python - Curso em vídeo

# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# Meu Código
print('*' * 29)
print(' ' * 6 + 'Menu de Opções!!!')
print('*' * 29)
op = 0
n1 = int(input('Digite o primeiro Valor: '))
n2 = int(input('Digite o segundo Valor: '))
while op != 5:
    print('*' * 35)
    print('''Selecione uma opção do Menu:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] novos números
    [ 5 ] Sair do programa''')
    op = int(input('Selecione a opção: '))
    print('*' * 35)
    if op == 1:
        print('A soma dos números {} + {} = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação dos números {} x {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O número {} é maior do que o {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior do que o {}'.format(n2, n1))
        else:
            print('Os números {} e {} são IGUAIS!'.format(n1, n2))
    elif op == 4:
        n1 = int(input('Digite o primeiro Valor: '))
        n2 = int(input('Digite o segundo Valor: '))
    else:
        print('Opção inválida! Tente novamente...')
print('Fim do programa!')

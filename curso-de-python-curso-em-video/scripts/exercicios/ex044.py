# Exercício 044 do curso de Python - Curso em vídeo

#  Elabore um programa que calcule o valor a ser pago por um produto,
#  considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

# Meu Código
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 31)
print(' ' * 3 + 'Gerenciador de Pagamento!')
print('*' * 31)
preco = float(input('Digite o valor da compra: '))
print('Formas de Pagamento')
print('[1] à vista dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] em até 2x no cartão')
print('[4] 3x ou mais no cartão')

op = int(input('Selecione a forma de pagamento: '))

if op == 1:
    preco = preco - (preco * 10 /100)
elif op == 2:
    preco = preco - (preco * 5 / 100)
elif op == 3:
    parc = int(input('Quantas parcelas? '))
    vparc = preco / parc
    print('Sua compra será parcelada em {} de {:.2f}. '.format(parc, vparc))
else:
    parc = int(input('Quantas parcelas? '))
    preco = preco + (preco * 20 /100)
    vparc = preco / parc
    print('Sua compra será parcelada em {} de {:.2f} com Juros. '.format(parc, vparc))
print('Seu produto vai custar R$ {:.2f} no final.'.format(preco))
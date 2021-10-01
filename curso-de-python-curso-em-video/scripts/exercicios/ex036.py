# Exercício 036 do curso de Python - Curso em vídeo

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Meu código
from time import sleep
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 30)
print(' ' * 4 + 'Aprovando Empréstimos!')
print('*' * 30)
vcasa = float(input('Digite o valor da casa: R$'))
vsalario = float(input('Digite o valor do salário: R$'))
anos = int(input('Digite em quantos anos pretende pagar: '))
parcela = vcasa / (anos * 12)
print('\nDados do Empréstimo!')
print('\nValor da casa {}R$ {:.2f}{}'.format(cores['red'], vcasa, cores['remove']))
print('Valor do salário {}R$ {:.2f}{}'.format(cores['g'], vsalario, cores['remove']))
print('Pagamento em {} anos com {}{}{} parcelas mensais de R$ {}{:.2f}{}'.format(anos, cores['g'], anos * 12, cores['remove'], cores['red'], parcela, cores['remove']))
print('Analisando...')
sleep(3)
if (parcela / vsalario) * 100 > 30:
    print('{}Que pena! Seu empréstimo foi Negado!{}'.format(cores['red'], cores['remove']))
else:
    print('{}Que Maravilha! Seu empréstimo foi Aprovado!{}'.format(cores['blue'], cores['remove']))

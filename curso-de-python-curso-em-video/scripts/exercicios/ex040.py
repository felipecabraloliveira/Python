# Exercício 040 do curso de Python - Curso em vídeo

#  Crie um programa que leia duas notas de um aluno e calcule sua média,
#  mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
from time import sleep
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 30)
print(' ' * 9 + 'Calculando Média!')
print('*' * 30)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('Analisando a média...')
sleep(1)
med = (n1 + n2) / 2
if med >= 7.0:
    print('Sua média foi de {:.2f}, {}Aprovado!{}'.format(med, cores['blue'], cores['remove']))
elif 5 <= med <= 6.99:
    print('Sua média foi de {:.2f}, {}Recuperação!{}'.format(med, cores['magenta'], cores['remove']))
else:
    print('Sua média foi de {:.2f}, {}Reprovado!{}'.format(med, cores['red'], cores['remove']))
# Correção - Ok
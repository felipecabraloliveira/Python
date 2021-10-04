# Exercício 040 do curso de Python - Curso em vídeo

#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
#  de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from time import sleep
from datetime import date
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 30)
print(' ' * 7 + 'Atleta Categoria!')
print('*' * 30)
nasc = int(input('Digite o ano de nascimento do atleta: '))
print('Analisando a categoria...')
sleep(1)
date = date.today()
year = date.strftime('%Y')
idade = int(year) - nasc
if idade <= 9:
    print('O atleta completa {} anos em {}, categoria: {}MIRIM!{}'.format(idade, year, cores['blue'], cores['remove']))
elif 9 < idade <= 14:
    print('O atleta completa {} anos em {}, categoria: {}INFANTIL!{}'.format(idade, year, cores['g'], cores['remove']))
elif 14 < idade <= 19:
    print('O atleta completa {} anos em {}, categoria: {}JÚNIOR!{}'
          .format(idade, year, cores['yellow'], cores['remove']))
elif 19 < idade <= 25:
    print('O atleta completa {} anos em {}, categoria: {}SÊNIOR!{}'.format(idade, year, cores['red'], cores['remove']))
else:
    print('O atleta completa {} anos em {}, categoria: {}MASTER!{}'
          .format(idade, year, cores['magenta'], cores['remove']))

# Exercício 039 do curso de Python - Curso em vídeo

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se
# já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
cores = {'blue': '\033[1;34m', 'red': '\033[1;31m', 'yellow': '\033[1;33m', 'g': '\033[1;32m',
         'magenta': '\033[1;35m', 'peb': '\033[1;30;107m', 'bep': '\033[1;97;40m', 'remove': '\033[0;0m'}
print('*' * 30)
print(' ' * 9 + 'Alistamento!')
print('*' * 30)
ano = int(input('Digite o ano de nascimento? '))
idade = 2021 - ano
data = date.today()
y = data.strftime('%Y')
print('Você nasceu em {} e completa {} anos em {}.'.format(ano, idade, y))
if idade > 18:
    tempo = 2021 - (ano + 18)
    print('O período de alistamento já passou!')
    print('{}O ano do seu alistamento foi em {}, você está atrasado há {} ano(s).{}'
          .format(cores['red'], int(y) - tempo, tempo, cores['remove']))
elif idade == 18:
    tempo = 0
    print('{} É a hora exata de se alistar!{}'.format(cores['blue'], cores['remove']))
else:
    tempo = (ano + 18) - 2021
    print('Você deve se alistar em breve!')
    print('{}O ano do seu alistamento é {}, faltam apenas {} ano(s) para se alistar!{}'
          .format(cores['g'], ano + 18, tempo, cores['remove']))

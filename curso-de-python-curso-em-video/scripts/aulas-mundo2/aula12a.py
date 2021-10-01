# Aula #12 - Condições Aninhadas
cores = {'red': '\033[1;31m', 'blue': '\033[1;34m', 'limpa': '\033[0m', 'cyan': '\033[1;36m', 'magenta': '\033[1;35m'}
nome = str(input('Qual é seu nome? ')).upper()
if nome == 'FELIPE':
    print('{}Que nome bonito!{}'.format(cores['magenta'], cores['limpa']))
elif nome == 'AUGUSTO' or nome == 'JESSICA' or nome == 'LARISSA':
    print('{}Nome até que legal!{}'.format(cores['blue'], cores['limpa']))
elif nome in 'PEDRO MARIA JOAO ANTONIO':
    print('{}Seu nome é bem Popular!{}'.format(cores['cyan'], cores['limpa']))
else:
    print('{}Seu nome é comum!{}'.format(cores['red'], cores['limpa']))

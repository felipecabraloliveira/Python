# Exercício 092 do curso de Python - Curso em vídeo

#  Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
#  (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
#  o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Meu Código
from datetime import datetime
print('=' * 37)
print(' ' * 2 + 'Cadastro de Trabalhador em Python')
print('=' * 37)

trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: ').title().strip())
nasc = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = datetime.now().year - nasc
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    # Corrigindo não é o ano, mas sim com que idade:
    trabalhador['Aposentadoria'] = (trabalhador['Contratação'] + 35) - nasc
    # Idade mínima considerando sexo masculino.
    if trabalhador['Aposentadoria'] < 65:
        trabalhador['Aposentadoria'] = 65
print('-=' * 30)
for i, v in trabalhador.items():
    print(f'{i}: {v}')
# Correção - Ok

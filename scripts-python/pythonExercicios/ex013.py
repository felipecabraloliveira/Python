# Exercicio 013 do curso de Python - Curso em vídeo

# Desenvolva um programa que leia o salário de um funcionário e mostre seu novo
# salário com 15% de aumento.

s = float(input('Digite o valor do salário atual: R$ '))
print('O salário foi de R${:.2f} para R${:.2f} obtendo 15% de aumento.'.format(s,s + (s/100*15)))

# Correção - OK

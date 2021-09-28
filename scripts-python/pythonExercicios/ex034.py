# Exercício 034 do curso de Python - Curso em vídeo

# Desenvolva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%
# Para inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite o salário do funcionário R$: '))
if s > 1250.00:
    print('O seu aumento é de 10%, novo salário: R${:.2f}'.format(s + (s * 10 /100) ))
else:
    print('O seu aumento é de 15%, novo salário: R${:.2f}'.format(s + (s * 15 / 100)))

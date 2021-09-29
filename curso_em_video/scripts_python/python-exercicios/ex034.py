# Exercício 034 do curso de Python - Curso em vídeo

# Desenvolva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%
# Para inferiores ou iguais, o aumento é de 15%.

# Meu Código
s = float(input('Digite o salário do funcionário? R$'))
if s > 1250.00:
    print('O seu aumento é de 10%, novo salário: R${:.2f}'.format(s + (s * 10 /100) ))
else:
    print('O seu aumento é de 15%, novo salário: R${:.2f}'.format(s + (s * 15 / 100)))

# Correção - Ok

print('\nOutra forma de atingir o objetivo!\n')
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1200:
    novo = salario + ( salario * 15 /100)
else:
    novo = salario + ( salario * 10 /100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

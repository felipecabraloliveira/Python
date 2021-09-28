# Exercício 029 do curso de Python - Curso em vídeo

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.

# Meu Código
v = float(input('Digite a velocidade do carro Km/h: '))
if v > 80:
    m = (v - 80) * 7
    print('Você ultrapassou o limite de velocidade e foi multado em R${:.2f} reais.'.format(m))
# Correção não possui a necessidade de utilizar o else:
print('Continue dirigindo no limite de velocidade de 80Km/h!')

# Correção - OK
print('\nOutra forma de atingir o objetivo!\n')
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

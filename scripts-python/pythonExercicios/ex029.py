# Exercício 029 do curso de Python - Curso em vídeo

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.

v = float(input('Digite a velocidade do carro Km/h: '))
if v > 80:
    m = (v - 80) * 7
    print('Você ultrapassou o limite de velocidade e foi multado em R$ {:.2f} reais.'.format(m))

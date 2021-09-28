# Exercício 031 do curso de Python - Curso em vídeo

# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de
# até 200Km e R$0,35 para viagens mais longas.

d = float(input('Digite a distância da viagem em Km: '))
if d <= 200:
    print('O preço da passagem  para uma viagem de {:.2f}Km é de R$: {:.2f} reais.'.format(d, d * 0.50))
else:
    print('O preço da passagem para uma viagem de {:.2f}Km é de R$: {:.2f} reais.'.format(d, d * 0.45))

# Exercício 031 do curso de Python - Curso em vídeo

# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de
# até 200Km e R$0,35 para viagens mais longas.

# Meu Código
d = float(input('Digite a distância da viagem em Km: '))
if d <= 200:
    print('O preço da passagem  para uma viagem de {:.2f}Km é de R${:.2f} reais.'.format(d, d * 0.50))
else:
    print('O preço da passagem para uma viagem de {:.2f}Km é de R${:.2f} reais.'.format(d, d * 0.45))

# Correção

print('\nOutra forma de atingir o objetivo!\n')
distancia = int(input('Qual é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''
# outra forma, if simplificado
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preco))

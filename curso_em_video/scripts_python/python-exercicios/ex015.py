# Exercicio 015 do curso de Python - Curso em vídeo

# Aluguel de carro - Escreva um programa que pergunte a quantidade de KM percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule
# o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

dias = int(input('Digite a quantidade de dias alugados: '))
km = float(input('Digite a quantidade de KMs percorridos: '))

print('Você percorreu {:.1f}KMs em {} dias, total a pagar R${:.2f}'.format(km,dias,km * 0.15 + dias * 60))

# Correção - Ok
# Exercicio 006 do curso de Python - Curso em vídeo

# Crie um algoritmo que leia um número e mostre o dobro, triplo e raiz quadrada.

# meu código

n = int(input('Digite um número: '))
print('Número digitado: {} \nDobro: {} \nTriplo: {} \nRaiz quadrada: {:.2f}'.format(n,n*2,n*3,n**(1/2)))

# Correção - OK

# Pode ser utilizado uma função interna para a raiz quadrada pow(n,(1/2))
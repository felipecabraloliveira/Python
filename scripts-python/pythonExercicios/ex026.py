# Exercicio 026 do curso de Python - Curso em vídeo

# Crie um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes aparece a letra 'A'
# 2 - Em que posição ela aparece a primeira vez.
# 3 - Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip() # Removendo espaços em branco.
print('Quantas vezes a letra A aparece na frase: {} vezes.'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição: {}'.format(frase.upper().find('A')))
print('A letra A aparece pela última vez na posição: {}'.format(frase.upper().rfind('A')))

# Correção - Ajustar a posição do caracter exibido.

print('\n\n***Outra forma de atingir os resultados!***')
print('Quantas vezes a letra A aparece na frase: {} vezes.'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição: {}'.format(frase.upper().find('A')+1))
print('A letra A aparece pela última vez na posição: {}'.format(frase.upper().rfind('A')+1))

# Exercicio 024 do curso de Python - Curso em vídeo

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da Cidade: ')).upper().strip()
# Alterando as letras digitados para maiúsculos e removendo espaços.
lista = cidade.split()
print('A cidade começa com SANTO: {}'.format('SANTO' in lista[0]))

# Correção

print('\n\n***Outra forma de atingir os resultados!***')
print(cidade[:5] == 'SANTO')

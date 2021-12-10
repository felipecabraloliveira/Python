# Exercício 077 do curso de Python - Curso em vídeo

#  Crie um programa que tenha uma tupla com várias palavras
#  (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
#  quais são as suas vogais.

# Meu Código
print('=' * 37)
print(' ' * 5 + 'Contando Vogais em Tupla!')
print('=' * 37)

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aáãâeéêiíoõuú':
            print(f'{letra.upper()} ', end='')
            
# Exercício 080 do curso de Python - Curso em vídeo

# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

print('=' * 37)
print(' ' * 4 + 'Lista ordenada sem repetições')
print('=' * 37)
valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao Final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados foram {valores}')
# Correçã - Ok

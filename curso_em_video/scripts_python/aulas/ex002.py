n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
soma = n1 + n2
print('Soma: ' ,soma)


# Ajustando a entrada de dados, pois ele interpetra o valor digitado como uma string

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('Soma: ' ,soma)

print('A soma vale {}'.format(soma)) # Sintaxe recente para exibir valores na tela.

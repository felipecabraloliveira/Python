n1 = input('Digite um valor: ')
print(type(n1))

# Digite um valor: 10
# <class 'str'>


n1 = int(input('Digite um valor: '))
print(type(n1))

# Digite um valor: 10
# <class 'int'>

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
#print('A soma entre', n1 , 'e', n2, 'vale', soma)
print('A soma entre {0} e {1} vale: {2}'.format(n1,n2,soma))

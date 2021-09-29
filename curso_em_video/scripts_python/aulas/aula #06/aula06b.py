n = float(input('Digite um valor: '))
print(n)

# Digite um valor: 10
# 10.0

n = bool(input('Digite um valor: '))
print(type(n))
print(n)

# Digite um valor: 10
# <class 'bool'>
# True - Se tem valor dentro é verdadeiro, caso não falso

n = input('Digite algo: ')
print('É um número:' ,n.isnumeric())
print('Possui apenas letras:' ,n.isalpha())
print('Alpha numerico:' ,n.isalnum())
print('Alpha numerico:' ,n.isupper())


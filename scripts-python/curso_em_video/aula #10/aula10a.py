nome = str(input('Qual é sue nome? ')).strip().upper()
if nome == 'FELIPE':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
print('\nComparando se a nota foi boa ou não utilizando uma condição composta!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim! Estude mais!')
print('\nUtilizando uma condição simples!')
print('Parabés' if m>=6 else 'Estude Mais!')

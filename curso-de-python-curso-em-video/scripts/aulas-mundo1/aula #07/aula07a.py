nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

print('Prazer em te conhecer {: ^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

print('A soma vale {}'.format(n1+n2))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 **n2

print('A soma é {},\no produto é {},\na divisão é {:.2}, '.format(s,m,d), end =' ')
print('divisão inteira é {} e a potência é {}'.format(di,e))

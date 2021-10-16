# Aula 14 do Curso de Python do Curso em Vídeo.

for c in range(1, 10):
    print(c)
print('Fim')

print('\n**** Utilizando o While ****')
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
print('\nUtilizando FOR')
# For é usado quando sabemos exatamente a quantidade de vezes que queremos que o laço se repita.
for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('Fim')
print('Utilizando While, repetindo o laço até que o valor digitado seja igual a 0.')
# While permite utilizarmos o laço sem determinar a quantidade de laços, pois ele vai
# receber o valor por meio do usuário por exemplo.
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

print('Questiona o seu usuário se ele quer continuar digitando ou não.')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quar Continuar? [s/n]: ')).upper()
print('Fim')

print('Verificando dos números digitados quantos são par e quantos são ímpares.')
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

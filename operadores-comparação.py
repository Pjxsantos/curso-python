x = y = z = float

n1 = n2 = 0

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

x = n1 == n2
print ('são iguais?', x,'\n')

z = n1 > n2
print ('é maior que ', n2, '?: ', z,'\n')

y = n1 != n2
print ('são diferentes?: ' + str(y))

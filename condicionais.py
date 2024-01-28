# Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))

# Caucular a média aritimetica das notas
media = (n1 + n2) / 2

if (media >= 7):
    print ("Resultado: Aprovado!")
    print ("Parabéns!")
elif (media >= 5):
    print ("Resultado: Recuperação!")
else:
    print ("Resultado: Reprovado!")
    print ("Que pena tente outra vez!")

print ('Sua média é {}'.format(media))
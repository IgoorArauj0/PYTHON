from random import randint
from time import sleep
n = randint(0, 5)
print('Vou pensar em um número de 0 à 5, tente adivinhar!')
sleep(1)
print('PROCESSANDO...')
sleep (2)
d = int(input('Em qual número eu pensei? R: '))
if d == n:
    print('Parabéns, você acertou! Eu realmente escolhi o número {}.'.format(n))
else:
    print('Você errou, que pena! O número que eu escolhi foi {}.'.format(n))
print('\nObrigado por participar do desafio!')

#Pedir para o PC dar um número aleatório de 0 à 5 e o usuário adivinhar.

from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print ('O ângulo de {} tem o seno de {:.2f}'.format(a, seno))
print ('O ângulo de {} tem o cosseno de {:.2f}'.format(a, cos))
print ('O ângulo de {} tem a tangente de {:.2f}'.format(a, tan))

#Ler o seno, cosseno e tangente de um ângulo.   
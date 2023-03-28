n = input('Digite seu nome: ')

print ('Este é o seu nome em letra MAIÚSCULA:',n.upper())
print ('Este é o seu nome em letra minúscula:',n.lower())
print ('Seu nome contém {} letras!'.format(len(n) - n.count(' ')))
print ('Seu primeiro nome tem {} letras!'.format(n.find(' ')))

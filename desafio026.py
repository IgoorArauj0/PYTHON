f = str(input('Digite uma frase: ')).upper().strip()
print ('A letra "A" nessa frase apareceram {} vezes!'.format(f.count('A'))) #Count = contar qnts vezes aparece
print ('A primeira letra "A" apareceu na posição {}.'.format(f.find('A')+1)) #Find = contar qnts posições antes de aparecer
print ('A última letra "A" apareceu na posição {}.'.format(f.rfind('A')+1))  #Rfind = contar a ultima vez q apareceu

#Ler uma frase e dizer quantas vezes a letra 'A' apareceu, qual a posição da primeira letra 'A' e a ultima posição

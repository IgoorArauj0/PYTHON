n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print ('Muito prazer em te conhecer!')
print ('O seu primeiro nome é: {}'.format(nome[0]))
print ('O seu último nome é: {}'.format(nome[len(nome)-1])) #LEN = Ultima posição

#lER O NOME DO USUÁRIO E SEPARAR PRIMEIRO E ULTIMO NOME
v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('Multado! Você ultrapassou o limite da via de 80Km/h.')
    m = ((v-80)*7)
    print('O valor da sua multa é de R${:.2f}.'.format(m))
print('Dirija com segurança, tenha um bom dia!')

#Leia a velocidade do carro e multe se ultrapassar dos 80km/h. O valor da multa é R$7,00 a cada 1km/h acima dos 80km/h.

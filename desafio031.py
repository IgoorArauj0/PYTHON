d = int(input('Digite a distância de sua viagem (em Km): '))
if d <= 200:
    c = d * (0.50)
    print('Você percorrerá {}Km. O valor da sua viagem será R${:.2f}'.format(d,c))
else:
    l = d * (0.45)
    print('Você percorrerá {}Km. O valor da sua viagem será R${:.2f}'.format(d,l))

# Leia a distância da viagem, até 200km cobre R$0,50 por Km, se for +200km cobre R$0,45 por Km.
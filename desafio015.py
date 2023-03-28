d = float(input("Quantas diárias você utilizou?: "))
k = float(input("Quantos Km você percorreu?: "))
dt = d*60
kt = k*0.15
print ("O valor total da diária ficou de R${:.2f} e por Km ficou de R${:.2f}. O valor total à pagar é: R${:.2f}.".format(dt,kt,dt+kt))

#Calcule a quantidade de km percorridos e a diária e diga o valor total (diária 60 reais o dia, 0.15 reais por KM
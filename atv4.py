d = float(input("Informe a distância de sua viagem: "))
c = float(input("Informe o consumo de seu carro por litro: "))
print("O valor da gasolina é R$5,49")
g = 5.49

ct = d/c*g 
ct = round(ct)

print("O valor total da viagem será: R${:.2f}".format(ct))
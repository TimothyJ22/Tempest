g = float(input("Informe o preço da gasolina: "))
a = float(input("Informe o preço do álcool: "))

r = a/g
s = r*100
s = round(s)

if (s <= 75):
 print("A relação entre o álcool e a gasolina é: {:.2f}, é mais vantajoso utilizar álcool".format(s))

elif(s > 75):
 print("A relação entre o álcool e a gasolina é: {:.2f}, é mais vantajoso utilizar gasolina".format(s))
 

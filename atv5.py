n = str(input("Insira o seu nome: "))
i = int(input("Insira a idade: "))
p = float(input("Insira o seu peso (kg): "))
a = float(input("Insira a sua altura (m): "))

r = p/(a*a)
r = round(r)

if (r <= 18.5):
    print("{},  seu IMC é: {}, você está abaixo do peso.".format(n,r))

elif (r <= 24.9):
    print("{}, o seu IMC é: {}, o seu peso é ideal.".format(n,r))

elif (r <= 29.9):
    print("{} o seu IMC é: {}, você está levemente acima do peso.".format(n,r))

elif (r <= 34.9):
    print("{}, o seu IMC é: {}, obesidade grau I.".format(n,r))    

elif (r <= 39.9):
    print("{}, o seu IMC é: {}, obesidade grau II (severo).".format(n,r))

elif (r >= 40):
    print("{}, o seu IMC é: {}, obesidade grau III (mórbido).".format(n,r))
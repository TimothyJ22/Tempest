n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))
n3 = int(input("Insira a terceira nota: "))
s = (n1+n2+n3)/3

if (s >= 6):
    print("Sua média final é: ", s, " parabéns")
elif (s < 6):
    print("Você está de exame")
else:
    print("Você passou!")

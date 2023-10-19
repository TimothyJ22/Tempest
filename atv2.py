n = str(input("Insira o seu nome: "))
i = int(input("Insira a idade: "))
p = float(input("Insira o seu peso (kg): "))
a = float(input("Insira a sua altura (m): "))

r = p/(a*a)

r = round(r)

print("O seu IMC é: {}".format(r))

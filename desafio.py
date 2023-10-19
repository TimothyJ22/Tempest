a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))
c = float(input("Insira o terceiro número: "))

dt = b**2 -(4*a*c)

x1 = -b + (dt**0.5)
x1 = x1 / (2*a)

x2 = -b + -(dt**0.5)
x2 = x2 / (2*a)

print("O valor de x1 é: {:.2f}, e de x2 é: {:.2f}".format(x1,x2))
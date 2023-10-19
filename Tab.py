h = int(input("Informe a tabuada que você deseja: "))
a = int(input("Informe até qual número você deseja fazer a tabuada: "))
a = a + 1

for n in range (1,a):
    l = h * n
    print(h, "x", n, "=", l)
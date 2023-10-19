c = 0
for q in range (0, 5):
    n = int(input("Digite um valor: "))
    if (n > 0):
        s = (n%2 == 0)
        c = c + 1

print("{} números positivos".format(c))
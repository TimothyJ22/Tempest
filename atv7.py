c = 0
p = 0
for q in range (0, 5):
    n = int(input("Digite um valor: "))
    if (n < 0):
        s = (n%2 == 0)
        c = c + 1
    else:
        p = p + 1

print("{} números negativos e {} números positivos".format(c, p))
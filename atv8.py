i = 0
p = 0
for q in range (5):
    n = int(input("Informe um número: "))
    if (n >= n%2 == 0):
        p = p + 1
    else:
        i = i + 1

print("São {} números pares e {} números ímpares ".format(p,i))

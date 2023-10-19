n = 1
num = int(input("informe o número desejado: "))
f = num

for q in range(n, num):
    f = f * n
    n = n + 1
print("O fatorial de {} é: {}".format(num, f))
n = 1
num = int(input("Digite um número: "))
f = num

while n < num:
    f = f * n
    n = n + 1
print("O fatorial de {} é: {}".format(num, f))
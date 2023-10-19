h = int(input("Informe a tabuada que você deseja: "))
a = int(input("Informe até onde você quer que seja: "))
n = 0

while n < a:
    n = n + 1
    r = h * n
    print("{} x {} = {}".format(h, n, r))
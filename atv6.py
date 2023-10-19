print("-------------------------------------------")
print("--------------- MÉDIA ANUAL ---------------")
print("-------------------------------------------")

n1 = int(input("Informe a primeira nota: "))
n2 = int(input("Informe a segunda nota: "))
n3 = int(input("Informe a terceira nota: "))
n4 = int(input("Informe a quarta nota: "))

ma = (n1+n2+n3+n4)/4

if (ma < 6):
    print("O seu conceito é 'C', você está reprovado.")
elif (ma < 8):
    print("O seu conceito é 'B', você está aprovado!")
elif (ma >= 8):
    print("O seu conceito é 'A', você está aprovado! Parabéns!")
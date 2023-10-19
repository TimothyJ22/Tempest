print("--------------- MENU ---------------")
print("")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")
print("")

opc = int(input("Insira uma opção: "))

if (opc <= 1):
    n1 = int(input("Insira o 1º número: "))
    n2 = int(input("Insira o 2º múmero: "))
    calc = n1+n2
    print("O resultado é: {:.2f}".format(calc))

elif (opc <= 2):
     n1 = int(input("Insira o 1º número: "))
     n2 = int(input("Insira o 2º múmero: "))
     calc = n1-n2
     print("O resultado é: {:.2f}".format(calc))
    
elif (opc <= 3):
     n1 = int(input("Insira o 1º número: "))
     n2 = int(input("Insira o 2º múmero: "))
     calc = n1*n2
     print("O resultado é: {:.2f}".format(calc))

elif (opc <= 4):
     n1 = int(input("Insira o 1º número: "))
     n2 = int(input("Insira o 2º múmero: "))
     calc = n1/n2
     print("O resultado é: {:.2f}".format(calc))

elif (opc <= 5):
     print("Ação terminada")

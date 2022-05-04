factorial = 1
numero=(input("ingresa numero"))
if (numero.isdigit()):
    numero=int(numero)
    for i in range (numero,1,-1):
        factorial = factorial * i
        print (factorial)
else:
    print("ingresa numero valido")


# hola mundo 
print ("Hola Mundo: ")

#control numero 9


print("escriba numero")
N=input()
if (N.isdigit()):
    N=int(N)
    if (N == 9):
        print(" numero es igual a 9")
    else:
        if (N>9):
            print("numero es mayor a 9")
        else:
            print("Numero es menor")
else:
    print("por favor ingrese valor numerico")
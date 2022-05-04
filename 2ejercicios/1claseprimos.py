#numeros primos 

nro = input("ingresa un numero")

if (nro.isdigit()):
    nro=int(nro)
    div = 2
    band = True
    if (nro == 1):
        print ("es primo")
    else:
        while (band and nro >div):
            if ( nro % div == 0):
                band = False
            div += 1

        if (band):
            print("es primo")
        else:
            print("no es primo")

else:
    print("ingrese numero valido")
# numeros primos 
numero = int(input("ingresa numero entero :"))
divisor = 2
band = True

if (numero == 1):
    print("Es primo")

else:
    while (band and numero > divisor):
        if (numero % divisor == 0):
            band = False
        divisor += 1
    
    if ( band ):
        print("es primo")
    else:
        print("no es primo")


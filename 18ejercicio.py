# divisores de numeros 

#print( " ingrese numero")
while(True):
    num = (input("ingrese numero"))
    if (num.isdigit()):
        num=float(num)
        div=1
        while (div <= num):
            if (num % div == 0):
                print (div)
            div= div+1
    # o div+=1
    #linea 9 seria igual a linea 10
    else:
        print("ingresa valor numerico" )
        
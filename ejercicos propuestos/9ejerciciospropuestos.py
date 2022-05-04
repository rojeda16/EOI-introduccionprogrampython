a=(input("ingrese numero comparador:"))
b=(input("ingrese numero a comparar:"))

if (a.isdigit() and b.isdigit()):
    b=int(b)
    a=int(a)
    if (b > a):
        print (f" el numero a comparar {b} es MAYOR que el numero comparador {a}")
    elif (a > b):
        print (f" el numero a comparar {b} es MENOR que el numero comparador {a}")
    else: print("ambos numeros  ingresados son iguales {a} y {b}" )
else: print("ingresa numeros validos para a y b")
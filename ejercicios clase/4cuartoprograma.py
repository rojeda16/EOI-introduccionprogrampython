mensaje = "dd"
ciudad = "alabacete"
print("hola {}".format(mensaje)) # no es eficiente
print("hola "  +  mensaje)
print("hola {m} de {c} " .format(m=mensaje,c=ciudad))
numero = 10/3
print("el numero es:{}".format(numero))
print("el numero es:{x}".format(x=numero))
print("el numero es:{n:1.2f}".format(n=numero))
print(f"hola {mensaje} de {ciudad}")

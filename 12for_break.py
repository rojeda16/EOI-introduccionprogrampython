contadordenumerosenlaserie=0
for numero in range(1,21,2):
    contadordenumerosenlaserie += 1
    if (contadordenumerosenlaserie>5):
        break #salte a la linea despues del bloque for numero in range 
    print(numero)
print("numeros de la serie", contadordenumerosenlaserie)
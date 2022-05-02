#lenguajes= ["python","c","c++","java"]

#for numero in range (4):
    #print (numero)
#for numero in range (1,4):
   # print (numero)
#for numero in range (1,11,3):
    #print (numero)
    


contadornumero=0
for numero in range (1,20,2):
    #print (numero)
    contadornumero+=1
    if (contadornumero<=5):
        continue
    print (numero)

contadordenumerosenlaserie=0
for numero in range(1,21,2):
    contadordenumerosenlaserie+=1
    if (contadordenumerosenlaserie<=5):
        
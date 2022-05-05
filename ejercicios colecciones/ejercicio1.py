from random import randint


listaH =[]
listaM =[]
for i in range(0,100):
   genero=randint(0,1)
   if (genero==0): listaM.append(genero)
   else:listaH.append(genero)
print(f"El porcentaje de mujeres es: {len(listaM)} %")
print(f"El porcentaje de hombres es: { len(listaH)} %")

if (len(listaM)>50):print(" Hay mas Mujeres")
elif(len(listaH)>50):print(" hay mas Hombres")
else: print("Hay Igualdad")




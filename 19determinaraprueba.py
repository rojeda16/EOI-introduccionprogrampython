# Aprueba_Suspende

#Cal1= float(input("Ingresa Calificacion numerica"))
#Cal2= float(input("Ingresa Calificacion numerica"))
#Cal3= float(input("Ingresa Calificacion numerica"))

#if (Cal1 <=11 and Cal2 <=11 and Cal3 <=11):
    #prom=(Cal1+Cal2+Cal3)/3
    #print(prom)

    
    #if (prom>=5):
    #    print("aprobado")
    #else:
    #    print("suspende")

#else:
#    print("ingrese calificacion valida")
        



#prueba 2



Cal1= (input("Ingresa Calificacion numerica"))
Cal2= (input("Ingresa Calificacion numerica"))
Cal3= (input("Ingresa Calificacion numerica"))

try:
    Cal1=float(Cal1)
    Cal2=float(Cal2)
    Cal3=float(Cal3)
    prom=(Cal1+Cal2+Cal3)/3
    if (prom >= 4):
        print(f"El alumno aprueba el curso. su media es de {prom}")
    else:
        print(f"El alumno suspende el curso. su media es de {prom}")

except ValueError:
    print("ingrese unas claificaciones numericas")
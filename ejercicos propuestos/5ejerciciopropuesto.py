
def areacilindro (h,r):
    area = 2*3.14*r*h + 2*3.14*r*r 
    return (area)


x = areacilindro(5,6)
print(x)




def volumencilindro (r,h):
    volumen = 3.14*r*r*h
    return (volumen)

y = volumencilindro(9,7)
print(y)



def factorial():
    x = int (input("ingresa numero"))
    res = x
    for i in range (x-1,1,-1):
        res=res*i
    print(res)

factorial()
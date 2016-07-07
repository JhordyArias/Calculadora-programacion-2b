import math    
def coseno(a):
    y=math.cos(a)
    return y
def arcoseno(b):
    if b>0-1 and b<=1:
        z=math.acos(b)
        w=math.degrees(z)
        return w
    else:
        print("----------------------------------")
        print("usted ingreso un numero no valido")
while True:
    x=input("Introdusca un angulo: ")
    if x.isdigit():
        x=float(x)
        break
    else:
        print("opcion no valida, vuelva a intentarlo")
while True:
    u=input("introdusca el numero (entre -1 y 1): ")
    if True:    
        u=float(u)
        break
    else:
        print("opcion no valida, vuelva a intentarlo")
        
print("el coseno es:{}".format(coseno(x)))
print("el arcocoseno es:{}°".format(arcoseno(u)))


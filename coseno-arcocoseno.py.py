import math
import time
def coseno(a):
    y=math.cos(a)
    return y
def arcoseno(b):
    if b>=-1 and b<=1:
        z=math.acos(b)
        w=math.degrees(z)
        return w
    else:
        print("----------------------------------")
        print("usted ingreso un ángulo no valido, ya que el arcocoseno esta en un rango unico de -1 hasta 1")
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

print("\t\tresultado....")
time.sleep(3)
print("el coseno de ",x," es:{}radianes".format(coseno(x)))
print("el arcocoseno de ",u," es:{}°".format(arcoseno(u)))


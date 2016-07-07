import math
import time
def resta(a,b):
    y=a-b
    return y
while True:
    e=input("Introdusca un primer numero: ")
    if e.isdigit():
        e=float(e)
        break
    else:
        print("opcion no valida, vuelva a intentarlo")
while True:
    i=input("introdusca el segundo numero: ")
    if i.isdigit():    
        i=float(i)
        break
    else:
        print("opcion no valida, vuelva a intentarlo")
print("\t\tresultado...")
time.sleep(3)
print("la resta total es:{}".format(resta(e,i)))


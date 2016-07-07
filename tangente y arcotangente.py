import math
def tang(d):
    x = math.tan(d)
    w = math.degrees(x)
    return w
def arctang(e):
    y = math.atan(e)
    z = math.degrees(y)
    return z
a = float(input('numero:'))
b = float(input('numeroo:'))
print('solucion: %.3f'%(tang(a)))
print('solucion: %.3f'%(arctang(b)))

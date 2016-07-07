import os
import sys
import time

def xalax():
    os.system("cls")
    print("Modelo: b^×\n*b: base.\n*×: exponente.")
    print("\nIngrese valor de la base:")
    while True:
        try:
            base = float(input())
            break
        except ValueError:
            print("BASE Ingresado no valido, intente nuevamente...")
    print("\nIngrese valor del exponente:")
    while True:
        try:
            exp = float(input())
            break
        except ValueError:
            print("EXPONENTE Ingresado no valido, intente nuevamente...")
    print()
    print(base ** exp)

xalax()
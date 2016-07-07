import os
import sys
import time

def menu():
    print("--- MENU ---")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Salir")

def pregunta():
    print("\n¿Desea realizar otra operacion?")
    while True:
        print("Si / No:")
        respuesta = input()
        if(respuesta.isalpha() == True and respuesta.lower() == "si" or respuesta.lower() == "no"):
            respuesta = respuesta.lower()
            break
        else:
            print("Opps! No era valido, intente nuevamente...")
    if(respuesta == "si"):
        os.system("clear")
        menu()
    if(respuesta == "no"):
        os.system("clear")
        print("Cerrando programa...")
        time.sleep(2)
        sys.exit(1)

pregunta()

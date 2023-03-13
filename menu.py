import os
import sys
import helpers
import database as db

def menu():
    while True:
        helpers.limpiar_pantalla()
        print("=====================================")
        print("=           MENU PRINCIPAL          =")
        print("=====================================")
        print("= 1. Crear punto                    =")
        print("= 2. Consultar cuadrante            =")
        print("= 3. Crear vector                   =")
        print("= 4. Consultar distancia            =")
        print("= 5. Listar puntos                  =")
        print("= 6. Crear rectangulo               =")
        print("=7. Salir                           =")
        print("=====================================")
        opcion = input("Seleccione una opcion: ")
        helpers.limpiar_pantalla()
        
        if opcion=="1":
            print("Has elegido la opción 1, crear punto")
            op=input("¿Desea continuar? (s/n): ")
            if op=="s":
                db.Punto_menu.crear_punto()
            else:
                print("Has elegido no continuar")

        elif opcion=="2":
            print("Has elegido la opción 2, consultar cuadrante")
            op=input("¿Desea continuar? (s/n): ")
            if op=="s":
                db.Punto_menu.cuadrante()
            else:
                print("Has elegido no continuar")

        elif opcion=="3":
            print("Has elegido la opción 3, crear vector")
            op=input("¿Desea continuar? (s/n): ")
            if op=="s":
                db.Punto_menu.vector()
            else:
                print("Has elegido no continuar")


        elif opcion=="4":
            print("Has elegido la opción 4, consultar distancia")
            op=input("¿Desea continuar? (s/n): ")
            if op=="s":
                db.Punto_menu.distancia()
            else:
                print("Has elegido no continuar")
                
        elif opcion=="5":
            db.Punto_menu.listar_puntos()
        elif opcion=="6":
            db.Punto_menu.crear_rectangulo()

        elif opcion=="7":
            helpers.limpiar_pantalla()
            print("=====================================")
            print("=           HASTA PRONTO            =")
            print("=====================================")

        input(">>> Presiona ENTER para continuar <<<")
        menu()
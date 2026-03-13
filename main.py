#/usr/bin/env python3

#Pa la Wera, siempre, todo. 
#Por las horas de diversión que pasamos jugando Moving Out!

from termcolor import colored
import signal
import sys

# módulos del script
from helpers.ayuda import paneldeAyuda
from helpers.rutas import seleccionarOrigen, seleccionarDestino
from helpers.archivos import seleccionarTipodeArchivo, obtenerExtensiones
from helpers.operaciones import moverArchivos, copiarArchivos, verArchivos
from helpers.eliminar import eliminar, eliminarporTamaño
from helpers.utils import salirdelPrograma

def def_handler(sig, frame):
    print(colored(f"[!]Saliendo...", 'red'))
    sys.exit(1)
signal.signal(signal.SIGINT, def_handler) #ctrl_c


def seleccionarAccion():
    print(colored(f"¡Bienvenide a MovingOut!", 'light_cyan'))
    
    while True:
        print(colored(f"¿Qué deseas hacer? \n", 'magenta'))
        print(colored(f"1. Mover archivos. \n2. Copiar archivos. \n3. Ver los archivos por consola. \n4. Eliminar los archivos. \n5. Abrir el panel de ayuda. \n6. Salir del programa", 'green'))
        
        accion=input(colored(f"Escribe el número de la acción: \n", 'green' ))
        
        if accion in ["1", "2", "3", "4"]:
            origen = seleccionarOrigen()
            destino = None
            if accion in ["1", "2"]:
                destino = seleccionarDestino()
            tipo = seleccionarTipodeArchivo()
            if tipo == "8":
                continue
            elif tipo == "9":
                salirdelPrograma()

            extension = obtenerExtensiones(tipo)
            if extension is None:
                continue

            if accion == "1":
                moverArchivos(origen, destino, extension)
            elif accion == "2":
                copiarArchivos(origen, destino, extension)
            elif accion == "3":
                verArchivos(extension, origen)
            elif accion == "4":
                porTamaño = input(colored("Desea añadir tamaño del archivo como criterio de eliminación (S/N): ", 'cyan'))
                if porTamaño.lower() == "s":
                    eliminarporTamaño(extension, origen)
                elif porTamaño.lower() == "n":
                    eliminar(extension, origen)
                else:
                    print(colored(f"Ha ocurrido un error, volveremos al menú principal", 'red'))
                    pass
        
        elif accion == "5":
            eleccion = paneldeAyuda()
            if eleccion == "1":
                seleccionarAccion()
            elif eleccion == "2":
                salirdelPrograma()
            else:
                print(colored(f"Opción inválida, volviendo al menú principal", 'red'))
                seleccionarAccion()

        elif accion == "6":
            salirdelPrograma()

        else:
            print(colored("Opción inválida, intenta de nuevo.", "red"))


if __name__ == "__main__":
    seleccionarAccion()



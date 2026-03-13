from termcolor import colored
import os
import shutil
from pathlib import Path

def eliminar(extension, origen):
    recursiva =input(colored("Desea que su búsqueda sea recursiva (S/N): ", 'cyan'))
    if recursiva.lower() == "s":
        try:
            for ext in extension:
                for archivos in Path(origen).rglob(f"*{ext}"):
                    os.remove(archivos)
        except Exception as e:
            print(colored(f"Ocurrió un error: {e}", 'red'))
    elif recursiva.lower() == "n":
        try:
            for ext in extension:
                for archivos in Path(origen).glob(f"*{ext}"):
                    os.remove(archivos)
        except Exception as e:
            print(colored(f"Ocurrió un error: {e}", 'red'))
    else:
        print(colored("Opción no válida. Volvamos a intentar.", 'red'))
        pass

def eliminarporTamaño (extension, origen):
        unidad = input(colored("Escribe la primera letra de la unidad de medida (Kilobytes, Megabytes, Gigabytes): ", 'cyan'))
        obtenerTamaño = int(input(colored("Escribe el tamaño: ", 'cyan')))
        criterio = input(colored("Se eliminarán archivos mayores(+), menores(-) o iguales(=) al tamaño pedido?: "))
        recursiva =input(colored("Desea que su búsqueda sea recursiva (S/N): ", 'cyan'))

        if unidad.lower() == "k":
            tamaño = obtenerTamaño * 1024
        elif unidad.lower() == "m":
            tamaño = obtenerTamaño * 1024 * 1024
        elif unidad. lower() == "g":
            tamaño = obtenerTamaño * 1024 * 1024 * 1024
        else:
            print(colored(f"ocurrió un error", 'red'))

        contador = []   
        if recursiva.lower() == "s":
            try:
                for ext in extension:
                    for archivo in Path(origen).rglob(f"*{ext}"):
                        if criterio in ["-", "menores"]:
                            if os.path.getsize(archivo) < tamaño:
                                contador.append(archivo)
                        elif criterio in ["+", "mayores"]:
                            if os.path.getsize(archivo) > tamaño:
                                contador.append(archivo)
                        elif criterio in ["=", "iguales"]:
                            if os.path.getsize(archivo) == tamaño:
                                contador.append(archivo)
                        else:
                            print(colored("Criterio inválido.", 'red'))
                confirmación = input(colored(f"Se eliminarán {len(contador)} archivos, ¿desea continuar (s/n)? "))
                if confirmación.lower() == "s":
                    for eliminaciones in contador:
                        os.remove(eliminaciones)
                else:
                    return None
            except Exception as e:
                print(f"Ha ocurrido un error {e}")
        elif recursiva.lower() == "n":
            try:
                for ext in extension:
                    for archivo in Path(origen).glob(f"*{ext}"):
                        if criterio in ["-", "menores"]:
                            if os.path.getsize(archivo) < tamaño:
                                contador.append(archivo)
                        elif criterio in ["+", "mayores"]:
                            if os.path.getsize(archivo) > tamaño:
                                contador.append(archivo)
                        elif criterio in ["=", "iguales"]:
                            if os.path.getsize(archivo) == tamaño:
                                contador.append(archivo)
                        else:
                            print(colored("Criterio inválido.", 'red'))
                confirmación = input(colored(f"Se eliminarán {len(contador)} archivos, ¿desea continuar (s/n)? "))
                if confirmación.lower() == "s":
                    for eliminaciones in contador:
                        os.remove(eliminaciones)
                else:
                    return None
            except Exception as e:
                print(f"Ha ocurrido un error {e}")
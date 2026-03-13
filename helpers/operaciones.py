from termcolor import colored
import os
import shutil
from pathlib import Path


def moverArchivos(origen, destino, extension):
    print(colored("[!]Tenga en cuenta que si en el destino existe algún archivo con el mismo nombre que alguno de los que se copiará, el archivo en la carpeta de destino será rescrito.", 'red'))
    recursiva = input(colored("Desea que su búsqueda sea recursiva (S/N): ", 'cyan'))
    if recursiva.lower() == "s":
        try:
            for ext in extension:
                for archivos in Path(origen).rglob(f"*{ext}"):
                    shutil.move(archivos, Path(destino) / archivos.name)
        except Exception as e:
            print(colored(f"Ocurrió un error: {e}", 'red'))
    elif recursiva.lower() == "n":
        try:
            for ext in extension:
                for archivos in Path(origen).glob(f"*{ext}"):
                    shutil.move(archivos, Path(destino) / archivos.name)
        except Exception as e:
            print(colored(f"Ocurrió un error: {e}", 'red'))
    else:
        print(colored("Opción no válida. Volvamos a intentar", 'red'))

def copiarArchivos(origen, destino, extension):
    print(colored("[!]Tenga en cuenta que si en el destino existe algún archivo con el mismo nombre que alguno de los que se copiará, el archivo en la carpeta de destino será rescrito.", 'red'))
    recursiva = input(colored("Desea que su búsqueda sea recursiva (S/N): ", 'cyan'))
    if recursiva.lower() == "s":
        try:
            for ext in extension:
                for archivos in Path(origen).rglob(f"*{ext}"):
                    shutil.copy(archivos, Path(destino) / archivos.name)
        except Exception as e:
            print(colored(f"Ocurrió un error: {e}", 'red'))
    elif recursiva.lower() == "n":
        try:
            for ext in extension:
                for archivos in Path(origen).glob(f"*{ext}"):
                    shutil.copy(archivos, Path(destino) / archivos.name)
        except Exception as e:
            print(colored(f"Ocurrió un error: {e}", 'red'))
    else:
        print(colored("Opción no válida. Volvamos a intentar", 'red'))

def verArchivos(extension, origen):
    recursiva =input(colored("Desea que su búsqueda sea recursiva (S/N): ", 'cyan'))
    encontrados = []
    if recursiva.lower() == "s":
        try:
            for ext in extension:
                for archivo in Path(origen).rglob(f"*{ext}"):
                    encontrados.append(archivo)
                    print(archivo)
            print(colored(f"Se han encontrado {len(encontrados)} archivos.", 'green'))
        except Exception as e:
            print(colored(f"Ocurrió un error: {e}", 'red'))
    elif recursiva.lower() == "n":
        try:
            for ext in extension:
                for archivo in Path(origen).glob(f"*{ext}"):
                    encontrados.append(archivo)
                    print(archivo)
            print(colored(f"Se han encontrado {len(encontrados)} archivos.", 'green'))
        except Exeption as e:
            print(colored(f"Ha ocurrido un error: {e}", 'red'))
    else:
        print(colored(f"Opción no válida. Volvamos a intentar.", 'red'))
        pass


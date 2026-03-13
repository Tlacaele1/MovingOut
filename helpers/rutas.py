from termcolor import colored
from pathlib import Path


def seleccionarOrigen():
    while True:
        origen=input("Escribe la ruta absoluta del directorio origen: ")
        if Path(origen).exists():
            return origen
        else:
            print(colored(f"La ruta especificada no existe.", 'red'))
        
def seleccionarDestino():
    print(colored(f"Ten en cuenta que si la ruta de destino no existe, se creará.", 'magenta'))
    while True:
        destino=Path(input("Escribe la ruta absoluta del directorio destino: "))
        if not destino.is_absolute():
            print(colored(f"Debes ingresar una ruta absoluta,", 'red'))
            continue
        try:
            destino.mkdir(exist_ok=True, parents=True)
            return destino
        except Exception as e:
            print(colored(f"Ha ocurrido un error {e}", 'red'))
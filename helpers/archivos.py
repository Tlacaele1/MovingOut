from termcolor import colored

def seleccionarTipodeArchivo():
    print(colored(f"Selecciona el tipo de archivo:\n", 'magenta'))
    print(colored(f"1. Imágenes.", 'green'))
    print(colored(f"2. Documentos.", 'green'))
    print(colored(f"3. Videos.", 'green'))
    print(colored(f"4. Audio.", 'green'))
    print(colored(f"5. Comprimidos.", 'green'))
    print(colored(f"6. Jácker.", 'green'))
    print(colored(f"7. Extensión personalizada.\n", 'green'))
    print(colored(f"8. Volver al menú principal.", 'red'))
    print(colored(f"9. Salir del programa.", 'red'))
    tipo=input(colored("Elige una opción: ", 'cyan'))
    return tipo

def obtenerExtensiones(tipo):
    tipos= {
        "1": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".tiff", ".psd", ".bmp"],
        "2": [".doc", ".pdf", ".docx", ".pptx", ".odp", ".txt", ".xls", ".xlsx", ".odt", ".csv", ".rtf"],
        "3": [".mpeg", ".mp4", ".mov", ".avi", ".wmv", ".mkv", ".flv", ".webm", ".m4v", ".3gp"],
        "4": [".mp3", ".wav", ".aac", ".wma", ".flac", ".aiff", ".ogg", ".m4a"],
        "5": [".gzip", ".7z", ".zip", ".rar", ".tar", ".bz2", ".xz"],
        "6": [".py", ".html", ".css", ".js", ".xml", ".php", ".sh", ".bat", ".pl", ".rb", ".json", ".r", ".ts", ".lua", ".ahk", ".cmd", ".ps1"]
    }
    if tipo == "7":
        extension=input(colored(f"Escribe la extensión precedida por un punto: ", 'cyan')).strip()
        return [extension.lower()]
    elif tipo in tipos:
        return tipos[tipo]
    else:
        print(colored(f"Opción inválida, volviendo al menú principal...", 'red'))
        return None
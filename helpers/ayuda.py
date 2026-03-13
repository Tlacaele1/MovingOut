from termcolor import colored    


def paneldeAyuda():
    print(colored(f"Este programa te ayuda a mover, copiar, ver en consola o eliminar los archivos de un mismo tipo dentro del directorio que elijas.", 'green'))
    print(colored(f"Para ello, tendrás que escribir la ruta absoluta del directorio donde quieres trabajar.\n", 'cyan'))
    print(colored(f"Ejemplos de ruta válida. \nEn linux: /home/usuario/desktop/documentos \nEn Windows C:\\Users\\usuario\\Pictures \n", 'magenta'))
    print(colored(f"Esta utilidad funciona con extensiones de archivo y contiene opciones para usar las extensiones más populares de un tipo de archivo: \n", 'green' ))
    print(colored(f"La opción imágenes utiliza jpg, jpeg, png, gif, webp, svg, tiff, psd, bmp.", 'cyan'))
    print(colored(f"La opción documentos utiliza doc, pdf, docx, pptx, odp, txt, xls, xlsx, odt, csv, rtf.", 'cyan'))
    print(colored(f"La opción videos utiliza mpeg, mp4, mov, avi, wmv, mkv, flv, webm, m4v, 3gp.", 'cyan'))
    print(colored(f"La opción audio utiliza mp3, wav, aac, wma, flac, aiff, ogg, m4a.", 'cyan'))
    print(colored(f"La opción comprimidos utiliza gzip, 7z, zip, rar, tar, bz2, xz.", 'cyan'))
    print(colored(f"La opción jácker utiliza py, html, css, js, xml, php, sh, bat, pl, rb, json, r, ts, lua, ahk, cmd, ps1.\n", 'cyan'))
    print(colored(f"Si la extensión que quieres no está en las opciones, o las opciones predeterminadas generan demasiado ruido, considera usar la opcion \"extensión personalizada\"", 'magenta'))
    print(colored(f"Esta opción te permitirá utilizar una extensión específica, para utilizarla simplemente elige el número 7 en el menú de extensiones y escribe la extensión de tu preferencia antecedida por un punto.\n", 'magenta'))
    print(colored(f"Las acciones mover y copiar, además del directorio origen, necesitarán la ruta absoluta de un directorio de destino.", 'green'))
    print(colored(f"Para ver ejemplos de rutas válidas, vuelva al comienzo de este panel.\n", 'red'))
    print(colored(f"Para cerrar en cualquier momento el flujo del programa, puedes usar las teclas ctrl+c\n",'green'))
    
    eleccion=input(colored(f"¿Qué desea hacer? \n 1. Volver al menú principal\n 2. Salir del programa \n", 'magenta'))
    return eleccion
    


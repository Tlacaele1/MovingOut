# MovingOut!

Utilidad de línea de comandos escrita en Python y diseñada para automatizar la gestión masiva de archivos.  
Originalmente creada para optimizar el post-procesamiento de datos recuperados mediante herramientas de informática forense (como **Photorec**), esta herramienta permite filtrar, organizar y limpiar grandes volúmenes de datos de forma recursiva y eficiente.

## Características:

* **Operaciones Masivas:** Mover, copiar, eliminar y visualizar archivos de forma recursiva.
* **Filtros Forenses:** Clasificación automática mediante diccionarios internos de extensiones comunes (Imágenes, documentos, ejecutables, etc.).
* **Limpieza por Tamaño:** Filtro avanzado para la opción de eliminar, permitiendo definir umbrales en `Kb`, `Mb` o `Gb` (ideal para descartar archivos residuales o dañados).
* **Nativo para Terminal:** Optimizado para flujos de trabajo en entornos Linux.
* **Búsqueda personalizada:** El programa permite la búsqueda por extensión personalizada. No estás sujeto a los diccionarios predefinidos.
* **Menú intuitivo:** El programa se maneja mediante un menú intuitivo e interactivo que te lleva paso a paso por cada fase del proceso.
* **Manejo de excepciones:** Las funciones se agrupan en bloques try-except para el manejo de excepciones y errores de modo que se evita el cierre abrupto.

## Requisitos:
* **termcolor** para la interfaz visual.
* **python3**

## Instalación
```bash
git clone [https://github.com/Tlacaele1/MovingOut.git](https://github.com/Tlacaele1/MovingOut.git)
cd MovingOut
pip3 install -r requirements.txt
```

## Estructura del proyecto:
```text
├── main.py              # Punto de entrada y ciclo principal
├── helpers/             # Paquete con lógica modular.
│   ├── archivos.py 	 # Diccionario de extensiones y menú de selección de extensiónes.
│   ├── ayuda.py	     # Panel de ayuda.
│   ├── eliminar.py      # Operación eliminar.
│   ├── operaciones.py   # Operaciónes mover, copiar y ver.
│   ├── rutas.py	     # Validación de las rutas proporcionadas por el usuario.  
│   └── utils.py	     # Salida del programa.  
├── requirements.txt
├── README.md
└── .gitignore           # Exclusión de archivos compilados (__pycache__)
```


## Uso:
```bash
python3 main.py
```

```markdown
---
*Pa la Wera, por las horas de diversión en Moving Out! y por ser el mejor soporte en cada línea de código.*
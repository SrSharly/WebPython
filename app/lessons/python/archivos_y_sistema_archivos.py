from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ArchivosSistemaArchivosLesson(Lesson):
    TITLE = "Archivos y sistema de archivos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    BADGES = ["⭐"]
    TAGS = [
        "archivos",
        "sistema de archivos",
        "open",
        "with",
        "read",
        "write",
        "FileNotFoundError",
    ]

    def summary(self) -> str:
        return (
            "Aprende a leer y escribir archivos de texto con open y with, "
            "y evita errores típicos como rutas inexistentes o modos incorrectos."
        )

    def guide(self) -> str:
        return """
## Introducción: archivos como memoria persistente
Los archivos guardan información fuera del programa. Cuando el programa termina, los datos siguen ahí. En Python,
la forma básica de trabajar con archivos es usar `open()` junto con `with` para cerrarlos automáticamente.

## Ejemplo principal (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** cómo escribir líneas en un archivo y leer su contenido completo.

**Haz esto (8–25 líneas con contexto):**
```py
ruta = "reporte.txt"
lineas = ["Ana,10\n", "Luis,7\n", "Sofía,12\n"]

with open(ruta, "w") as archivo:
    for linea in lineas:
        archivo.write(linea)

with open(ruta, "r") as archivo:
    contenido = archivo.read()

print(contenido.strip())
```

**Verás esto (salida real):**
```
Ana,10
Luis,7
Sofía,12
```

**Por qué funciona:** `open` abre el archivo en modo escritura y lectura; `with` asegura el cierre; `write` agrega
líneas; `read` recupera todo el texto.

**Lo típico que sale mal (error real):**
```py
with open("no_existe.txt", "r") as archivo:
    contenido = archivo.read()
```
```
FileNotFoundError: [Errno 2] No such file or directory: 'no_existe.txt'
```
Solución: crea el archivo antes, usa un modo adecuado (`"w"` o `"a"`) o verifica la ruta.

## Modos de apertura que usarás todo el tiempo
- `"r"`: lectura (falla si el archivo no existe).
- `"w"`: escritura (crea y sobrescribe).
- `"a"`: añadir al final (crea si no existe).

### Micro-ejemplo correcto: añadir sin borrar
```py
with open("log.txt", "a") as archivo:
    archivo.write("Nueva línea\n")
```

### Micro-ejemplo incorrecto: escribir en modo lectura
```py
with open("log.txt", "r") as archivo:
    archivo.write("No se puede")
```
```
io.UnsupportedOperation: not writable
```
Corrección: abre el archivo con `"w"` o `"a"` cuando necesites escribir.

### Micro-ejemplo correcto: leer solo una parte
```py
with open("log.txt", "r") as archivo:
    primeros = archivo.read(5)
```

### Micro-ejemplo incorrecto: pasar ruta inválida
```py
open(123, "r")
```
```
TypeError: expected str, bytes or os.PathLike object, not int
```
Corrección: la ruta debe ser texto (`str`) o un objeto de ruta válido.

## Glosario rápido (panel derecho)
- `open` → ver glosario.
- `with` → ver glosario.
- `read` → ver glosario.
- `write` → ver glosario.
- `FileNotFoundError` → ver glosario.
- `UnsupportedOperation` → ver glosario.

## Checklist final
- ¿Abriste el archivo con el modo correcto (`r`, `w`, `a`)?
- ¿Usaste `with` para cerrar automáticamente?
- ¿Manejaste el caso en que la ruta no existe?
- ¿Separaste lectura y escritura cuando aplica?
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Abrir en modo incorrecto",
                "Solución: usa 'r' para leer, 'w' para escribir y 'a' para añadir.",
            ),
            (
                "Olvidar usar with",
                "Solución: usa with open(...) para cerrar automáticamente el archivo.",
            ),
            (
                "Escribir y leer sin separar",
                "Solución: cierra el archivo y vuelve a abrirlo antes de leer.",
            ),
            (
                "Rutas inexistentes",
                "Solución: verifica la ruta o crea el archivo con 'w' o 'a'.",
            ),
            (
                "Usar rutas como números",
                "Solución: pasa siempre un string o un objeto de ruta.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Escritura y lectura básica",
                """ruta = "archivo.txt"
with open(ruta, "w") as archivo:
    archivo.write("Hola\n")
    archivo.write("Mundo\n")

with open(ruta, "r") as archivo:
    contenido = archivo.read()

print(contenido)""",
            ),
            (
                "Añadir sin sobrescribir",
                """with open("log.txt", "a") as archivo:
    archivo.write("Nueva línea\n")""",
            ),
            (
                "Lectura parcial",
                """with open("datos.txt", "r") as archivo:
    primeros = archivo.read(10)
print(primeros)""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un archivo llamado notas.txt y escribe tres líneas.",
                "hints": ["Usa open con modo 'w'.", "Escribe cada línea con write()."],
                "solution": (
                    "with open('notas.txt', 'w') as archivo:\n"
                    "    archivo.write('Línea 1\\n')\n"
                    "    archivo.write('Línea 2\\n')\n"
                    "    archivo.write('Línea 3\\n')"
                ),
            },
            {
                "question": "Lee el contenido de notas.txt y muéstralo por pantalla.",
                "hints": ["Usa open con modo 'r'.", "Usa read()."],
                "solution": (
                    "with open('notas.txt', 'r') as archivo:\n"
                    "    contenido = archivo.read()\n"
                    "print(contenido)"
                ),
            },
            {
                "question": "Añade una línea final a notas.txt sin borrar lo anterior.",
                "hints": ["Usa el modo 'a'.", "Escribe con write()."],
                "solution": (
                    "with open('notas.txt', 'a') as archivo:\n"
                    "    archivo.write('Línea extra\\n')"
                ),
            },
            {
                "question": "Maneja el error si intentas leer un archivo inexistente.",
                "hints": ["Captura FileNotFoundError.", "Muestra un mensaje claro."],
                "solution": (
                    "try:\n"
                    "    with open('fantasma.txt', 'r') as archivo:\n"
                    "        contenido = archivo.read()\n"
                    "except FileNotFoundError:\n"
                    "    print('Archivo no encontrado')"
                ),
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Practica creando y leyendo archivos de texto."))
        return widget

from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ArchivosSistemaLesson(Lesson):
    TITLE = "Archivos y sistema de archivos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["⭐"]
    TAGS = ["archivos", "filesystem", "rutas", "open", "pathlib"]

    def summary(self) -> str:
        return (
            "Aprende a leer y escribir archivos sin romper tu app: rutas relativas y "
            "absolutas, modos de apertura, encoding y el uso de pathlib."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## ¿Por qué esto es clave?
Leer y escribir archivos es una de las tareas más comunes en Python: configs, logs, datos y exportaciones. Si te equivocas
con una ruta o un modo de apertura, puedes perder información o bloquear el flujo del programa.

## Conceptos base: rutas
Una **ruta relativa** depende de la carpeta actual donde se ejecuta el programa. Una **ruta absoluta** empieza desde la raíz
del sistema.

**Micro-ejemplo correcto**
```py
ruta_relativa = "datos/usuarios.txt"
```

**Micro-ejemplo incorrecto**
```py
ruta_relativa = datos/usuarios.txt
```

**Error real**
```
NameError: name 'datos' is not defined
```

**Cómo se corrige**
Las rutas son texto: encierra la ruta en comillas.

## Abrir archivos con `open`
`open()` devuelve un manejador de archivo que debes usar dentro de un `with`.

**Micro-ejemplo correcto**
```py
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

**Micro-ejemplo incorrecto**
```py
with open("datos.txt", "rr") as archivo:
    contenido = archivo.read()
```

**Error real**
```
ValueError: invalid mode: 'rr'
```

**Cómo se corrige**
Usa modos válidos: `"r"` leer, `"w"` sobrescribir, `"a"` añadir.

## Ejemplo grande con contexto (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** guardar una lista de tareas en un archivo y volver a leerla sin perder caracteres especiales.

**Haz esto (ejemplo completo con contexto):**
```py
tareas = ["comprar pan", "estudiar Python", "caminar"]

with open("tareas.txt", "w", encoding="utf-8") as archivo:
    for tarea in tareas:
        archivo.write(tarea + "\\n")

with open("tareas.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.read().split("\\n")
    tareas_limpias = [linea.strip() for linea in lineas if linea.strip()]

print("Tareas:", tareas_limpias)
```

**Verás esto (salida real):**
```
Tareas: ['comprar pan', 'estudiar Python', 'caminar']
```

**Por qué funciona:** `open()` abre el archivo, `write()` escribe línea por línea, `read()` recupera todo el contenido,
`split()` separa por saltos de línea y `strip()` limpia espacios.

**Lo típico que sale mal (con error real):**
```py
with open("tareas.txt", "r") as archivo:
    contenido = archivo.write("hola")
```
```
io.UnsupportedOperation: not writable
```
Solución: usa el modo `"w"` o `"a"` si vas a escribir.

## Modos de apertura y errores típicos
### Lectura (`"r"`)
**Correcto**
```py
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

**Incorrecto**
```py
with open("no_existe.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

**Error real**
```
FileNotFoundError: [Errno 2] No such file or directory: 'no_existe.txt'
```

### Escritura (`"w"`) y anexado (`"a"`)
**Correcto**
```py
with open("log.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Nueva línea\\n")
```

**Incorrecto**
```py
with open("log.txt", "w", encoding="utf-8") as archivo:
    archivo.write(123)
```

**Error real**
```
TypeError: write() argument must be str, not int
```

**Cómo se corrige**
Convierte a texto con `str()` o usa f-strings.

## `pathlib` para rutas más claras
`pathlib` ayuda a construir rutas sin errores de separadores.

**Micro-ejemplo correcto**
```py
from pathlib import Path

ruta = Path("datos") / "usuarios.txt"
```

**Micro-ejemplo incorrecto**
```py
from pathlib import Path

ruta = Path("datos") + "usuarios.txt"
```

**Error real**
```
TypeError: unsupported operand type(s) for +: 'PosixPath' and 'str'
```

**Cómo se corrige**
Usa el operador `/` para unir rutas en `Path`.

### Lectura y escritura rápida con `Path`
**Correcto**
```py
from pathlib import Path

ruta = Path("notas.txt")
if ruta.exists():
    contenido = ruta.read_text(encoding="utf-8")
```

**Incorrecto**
```py
from pathlib import Path

ruta = Path("notas.txt")
contenido = ruta.read_text()
```

**Error real**
Si el archivo no existe, obtendrás:
```
FileNotFoundError: [Errno 2] No such file or directory: 'notas.txt'
```

## Checklist final
- Usas `with` para cerrar archivos automáticamente.
- Indicas `encoding="utf-8"` cuando trabajas con texto.
- Diferencias rutas relativas y absolutas.
- Evitas concatenar rutas con `+`; usa `Path`.
"""

    def build(self) -> QWidget:
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Archivos y sistema de archivos"))
        layout.addStretch()
        container = QWidget()
        container.setLayout(layout)
        return container

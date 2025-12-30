from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ArchivosSistemaLesson(Lesson):
    TITLE = "Archivos y sistema de archivos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Intermedio"
    BADGES = ["⭐"]
    TAGS = ["archivos", "rutas", "pathlib", "open", "io"]

    def summary(self) -> str:
        return (
            "Aprende a leer y escribir archivos de texto con seguridad, manejar rutas con "
            "pathlib y evitar errores típicos al trabajar con el sistema de archivos."
        )

    def guide(self) -> str:
        return """
## Por qué importa el sistema de archivos
Los archivos son la forma más común de **persistir datos**: reportes, logs, configuraciones y
salidas intermedias. Dominar `open()` y `pathlib` evita pérdidas de datos y errores silenciosos.

## Conceptos clave (sin asumir nada)
- **ruta (path)**: ubicación de un archivo o carpeta.
- **archivo de texto**: contenido legible con caracteres (UTF-8 es el estándar).
- **modo de apertura**: indica si lees (`"r"`), escribes (`"w"`) o agregas (`"a"`).

## Ejemplo grande con contexto (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** leer un archivo, filtrar líneas útiles y escribir un resumen nuevo.

**Haz esto (ejemplo completo con contexto):**
```py
from pathlib import Path

ruta_entrada = Path("datos/notas.txt")
ruta_salida = Path("salidas/resumen.txt")

lineas = ruta_entrada.read_text(encoding="utf-8").splitlines()
notas = [linea for linea in lineas if linea.strip()]

promedio = sum(float(n) for n in notas) / len(notas)

ruta_salida.parent.mkdir(parents=True, exist_ok=True)
ruta_salida.write_text(f"Promedio: {promedio:.2f}\n", encoding="utf-8")

print("Listo, resumen creado.")
```

**Verás esto (salida real):**
```
Listo, resumen creado.
```

**Por qué funciona:** `read_text()` lee todo el archivo como texto, `splitlines()` separa líneas,
`mkdir()` crea la carpeta de salida si no existe y `write_text()` guarda el resultado.

**Lo típico que sale mal (con error real):**
```py
ruta_entrada = Path("datos/notas.txt")
texto = ruta_entrada.read_text()
```
```
FileNotFoundError: [Errno 2] No such file or directory: 'datos/notas.txt'
```
Solución: verifica la ruta con `ruta_entrada.exists()` o crea el archivo antes de leer.

## Paso 1: usar open() con with (seguro y claro)
**Aprende esto:** `with` cierra el archivo aunque haya errores.

**Micro-ejemplo correcto**
```py
with open("notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

**Micro-ejemplo incorrecto**
```py
archivo = open("notas.txt", "r")
contenido = archivo.read()
```

**Error real**
```
ResourceWarning: unclosed file
```

**Cómo se corrige:** usa `with` para asegurar `close()` automático.

## Paso 2: modos de apertura y lo que realmente hacen
- `"r"`: lee (falla si no existe).
- `"w"`: escribe y **borra** el contenido anterior.
- `"a"`: agrega al final sin borrar.

**Micro-ejemplo correcto**
```py
with open("log.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Nueva línea\n")
```

**Micro-ejemplo incorrecto**
```py
with open("log.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Solo esta línea\n")
```

**Error real**
```
No hay error, pero se perdió el contenido anterior.
```

**Cómo se corrige:** usa `"a"` si necesitas conservar el historial.

## Paso 3: rutas con pathlib (evita errores por barras)
`pathlib` crea rutas multiplataforma y legibles.

**Micro-ejemplo correcto**
```py
from pathlib import Path

base = Path("datos")
ruta = base / "clientes" / "lista.txt"
```

**Micro-ejemplo incorrecto**
```py
ruta = "datos" + "/" + "clientes" + "/" + "lista.txt"
```

**Error real**
```
No hay error inmediato, pero en Windows puede fallar por separadores.
```

**Cómo se corrige:** usa `Path` para construir rutas.

## Paso 4: comprobar existencia antes de leer
**Micro-ejemplo correcto**
```py
ruta = Path("config/app.ini")
if ruta.exists():
    contenido = ruta.read_text(encoding="utf-8")
```

**Micro-ejemplo incorrecto**
```py
ruta = Path("config/app.ini")
contenido = ruta.read_text()
```

**Error real**
```
FileNotFoundError: [Errno 2] No such file or directory: 'config/app.ini'
```

**Cómo se corrige:** valida con `exists()` o crea el archivo con `write_text()`.

## Paso 5: crear archivos sin sobrescribir (modo "x")
**Aprende esto:** el modo `"x"` crea el archivo y falla si ya existe, evitando pérdida de datos.

**Micro-ejemplo correcto**
```py
with open("reportes/enero.txt", "x", encoding="utf-8") as archivo:
    archivo.write("Reporte creado\n")
```

**Micro-ejemplo incorrecto**
```py
with open("reportes/enero.txt", "x", encoding="utf-8") as archivo:
    archivo.write("Intento duplicado\n")
```

**Error real**
```
FileExistsError: [Errno 17] File exists: 'reportes/enero.txt'
```

**Cómo se corrige:** usa `"a"` si quieres agregar o elimina el archivo previo si necesitas regenerarlo.

## Paso 6: leer línea por línea sin cargar todo
**Aprende esto:** iterar el archivo evita cargarlo completo en memoria.

**Micro-ejemplo correcto**
```py
with open("logs/app.log", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())
```

**Micro-ejemplo incorrecto**
```py
with open("logs/app.log", "r", encoding="utf-8") as archivo:
    pass

archivo.read()
```

**Error real**
```
ValueError: I/O operation on closed file.
```

**Cómo se corrige:** realiza la lectura dentro del bloque `with`.

## Paso 7: encoding explícito para evitar caracteres rotos
**Aprende esto:** declara siempre el `encoding` cuando leas o escribas texto.

**Micro-ejemplo correcto**
```py
from pathlib import Path

ruta = Path("datos/correos.txt")
texto = ruta.read_text(encoding="utf-8")
```

**Micro-ejemplo incorrecto**
```py
from pathlib import Path

ruta = Path("datos/correos.txt")
texto = ruta.read_text()
```

**Error real**
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 12: invalid continuation byte
```

**Cómo se corrige:** especifica `encoding` al leer o escribir y evita mezclar archivos en
distintas codificaciones sin control.

## Paso 8: permisos del sistema y rutas protegidas
**Aprende esto:** algunas carpetas requieren permisos elevados.

**Micro-ejemplo correcto**
```py
from pathlib import Path

ruta = Path("salidas/reporte.txt")
ruta.parent.mkdir(parents=True, exist_ok=True)
ruta.write_text("ok\n", encoding="utf-8")
```

**Micro-ejemplo incorrecto**
```py
from pathlib import Path

ruta = Path("/root/reporte.txt")
ruta.write_text("ok\n", encoding="utf-8")
```

**Error real**
```
PermissionError: [Errno 13] Permission denied: '/root/reporte.txt'
```

**Cómo se corrige:** escribe en rutas donde tu usuario tenga permisos o ajusta permisos
de forma segura.

## Ejemplo ampliado con contexto: copiar y limpiar texto
**Aprende esto:** leer línea por línea y guardar solo lo útil.

**Haz esto (8–25 líneas con contexto):**
```py
from pathlib import Path

entrada = Path("datos/clientes.txt")
salida = Path("salidas/clientes_limpios.txt")

lineas = entrada.read_text(encoding="utf-8").splitlines()
limpias = [linea.strip() for linea in lineas if linea.strip()]

salida.parent.mkdir(parents=True, exist_ok=True)
salida.write_text("\n".join(limpias) + "\n", encoding="utf-8")

print("Clientes limpios:", len(limpias))
```

**Verás esto (salida real):**
```
Clientes limpios: 12
```

**Por qué funciona:** `strip()` elimina espacios, `join()` reescribe las líneas sin blancos extra.

**Lo típico que sale mal (con error real):**
```py
salida.write_text(limpias)
```
```
TypeError: write_text() argument must be str, not list
```
Solución: convierte la lista a texto con `"\n".join(limpias)`.

## Checklist final
- ¿Usaste `with` para cerrar el archivo automáticamente?
- ¿Elegiste el modo correcto (`r`, `w`, `a`)?
- ¿Necesitabas `"x"` para evitar sobrescribir un archivo existente?
- ¿Construiste rutas con `Path`?
- ¿Validaste existencia con `exists()`?
- ¿Definiste `encoding="utf-8"` para evitar caracteres raros?
- ¿Leíste por líneas si el archivo es grande?

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Abrir con 'w' cuando querías conservar datos",
                "El modo 'w' sobrescribe. Usa 'a' o 'r' según el caso.",
            ),
            (
                "No usar with",
                "Deja archivos abiertos; con with se cierran automáticamente.",
            ),
            (
                "Construir rutas con strings",
                "Usa Path para evitar fallos entre sistemas operativos.",
            ),
            (
                "Leer sin comprobar existencia",
                "Valida con exists() para evitar FileNotFoundError.",
            ),
            (
                "Leer fuera del bloque with",
                "El archivo ya está cerrado; mueve la lectura dentro del with.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Leer un archivo completo",
                """with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
print(contenido)""",
            ),
            (
                "Escribir varias líneas",
                """lineas = ["uno", "dos", "tres"]
with open("salida.txt", "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(lineas) + "\n")""",
            ),
            (
                "Crear carpetas con pathlib",
                """from pathlib import Path

ruta = Path("salidas") / "reporte.txt"
ruta.parent.mkdir(parents=True, exist_ok=True)
ruta.write_text("Reporte listo\n", encoding="utf-8")""",
            ),
            (
                "Comprobar si existe un archivo",
                """from pathlib import Path

ruta = Path("config.ini")
print(ruta.exists())""",
            ),
            (
                "Crear un archivo solo si no existe",
                """with open("reporte.txt", "x", encoding="utf-8") as archivo:
    archivo.write("Reporte inicial\\n")""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Lee un archivo y cuenta cuántas líneas no están vacías.",
                "hints": ["Usa read_text().splitlines()"],
                "solution": (
                    "from pathlib import Path\n"
                    "ruta = Path('datos.txt')\n"
                    "lineas = ruta.read_text(encoding='utf-8').splitlines()\n"
                    "no_vacias = [l for l in lineas if l.strip()]\n"
                    "print(len(no_vacias))"
                ),
            },
            {
                "question": "Agrega una línea al final de un archivo de log.",
                "hints": ["Abre con modo 'a' y usa write()."],
                "solution": (
                    "with open('log.txt', 'a', encoding='utf-8') as archivo:\n"
                    "    archivo.write('Nueva línea\\n')"
                ),
            },
            {
                "question": "Crea una carpeta 'salidas' y escribe un archivo dentro.",
                "hints": ["Usa Path(...).parent.mkdir(...)."],
                "solution": (
                    "from pathlib import Path\n"
                    "ruta = Path('salidas') / 'resultado.txt'\n"
                    "ruta.parent.mkdir(parents=True, exist_ok=True)\n"
                    "ruta.write_text('OK\\n', encoding='utf-8')"
                ),
            },
        ]

    def build_demo(self) -> QWidget:
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Practica rutas con pathlib y lectura segura con with."))
        container = QWidget()
        container.setLayout(layout)
        return container

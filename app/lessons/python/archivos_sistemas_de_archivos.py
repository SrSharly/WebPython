from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class ArchivosSistemasArchivosLesson(Lesson):
    TITLE = "Archivos y sistemas de archivos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    BADGES = ["⭐"]
    TAGS = ["archivos", "open", "read", "write", "with", "rutas"]

    def summary(self) -> str:
        return (
            "Aprende a leer y escribir archivos con seguridad, entender rutas, "
            "y evitar errores clásicos como archivos inexistentes o datos no guardados."
        )

    def guide(self) -> str:
        return """
## Introducción: por qué los archivos son básicos
Los archivos te permiten **persistir información**: guardar datos, configuraciones, reportes o
logs que sobreviven a la ejecución. Si no dominas lectura y escritura, tu programa pierde memoria
cuando termina.

## Conceptos previos (sin asumir nada)
- **variable**: nombre que apunta a un valor.
- **función**: bloque reutilizable de código.
- **método**: función asociada a un objeto.
- **with**: bloque que gestiona recursos automáticamente.
- **open**: función para abrir archivos y obtener un manejador.

### Buenas prácticas (CalloutBox: best_practice)
- Usa `with` siempre que puedas: asegura el cierre del archivo incluso si hay error.
- Sé explícito con el modo (`"r"`, `"w"`, `"a"`).
- Trabaja con rutas claras y consistentes.

## Paso 1: abrir un archivo con `open`
Para leer o escribir, primero necesitas abrir el archivo.

**Micro-ejemplo correcto**
```py
archivo = open("notas.txt", "r")
contenido = archivo.read()
archivo.close()
```

**Micro-ejemplo incorrecto**
```py
contenido = archivo.read()
```

**Error real**
```
NameError: name 'archivo' is not defined
```

**Corrección**
Debes abrir el archivo con `open()` antes de usar `read()`.

## Paso 2: `with` para cerrar automáticamente
`with` crea un bloque seguro que cierra el archivo al salir.

**Micro-ejemplo correcto**
```py
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
```

**Micro-ejemplo incorrecto**
```py
with open("notas.txt", "r") as archivo:
contenido = archivo.read()
```

**Error real**
```
IndentationError: expected an indented block after 'with' statement
```

**Corrección**
Indenta el bloque `with` y mantén el código dentro.

## Paso 3: modos de apertura (`r`, `w`, `a`)
El modo define qué operaciones puedes hacer.

**Micro-ejemplo correcto**
```py
with open("registro.txt", "a") as archivo:
    archivo.write("Nuevo evento\\n")
```

**Micro-ejemplo incorrecto**
```py
with open("registro.txt", "r") as archivo:
    archivo.write("Nuevo evento\\n")
```

**Error real**
```
UnsupportedOperation: not writable
```

**Corrección**
Para escribir usa `"w"` (sobrescribe) o `"a"` (agrega).

## Paso 4: leer con `read`, `readline` y `readlines`
Cada método sirve para un caso distinto.

**Micro-ejemplo correcto**
```py
with open("datos.txt", "r") as archivo:
    primera_linea = archivo.readline()
```

**Micro-ejemplo incorrecto**
```py
with open("datos.txt", "r") as archivo:
    primera_linea = archivo.readline[0]
```

**Error real**
```
TypeError: 'builtin_function_or_method' object is not subscriptable
```

**Corrección**
Llama al método con paréntesis: `archivo.readline()`.

## Ejemplo grande con contexto (Aprende esto → Haz esto → Verás esto)
**Aprende esto:** leer datos, filtrar contenido y guardar un reporte simple.

**Haz esto (ejemplo completo con contexto):**
```py
lineas = ["Ana,90", "Luis,70", "Marta,95"]

with open("notas.csv", "w") as archivo:
    for linea in lineas:
        archivo.write(linea + "\\n")

aprobados = []
with open("notas.csv", "r") as archivo:
    for linea in archivo.readlines():
        nombre, nota = linea.strip().split(",")
        if int(nota) >= 80:
            aprobados.append(nombre)

with open("reporte.txt", "w") as archivo:
    archivo.write("Aprobados:\\n")
    for nombre in aprobados:
        archivo.write(f"- {nombre}\\n")

print("Reporte generado:", aprobados)
```

**Verás esto (salida real):**
```
Reporte generado: ['Ana', 'Marta']
```

**Por qué funciona:** `write()` guarda datos, `readlines()` lee línea por línea y `with` cierra
cada archivo al terminar. Separas responsabilidades: escribir, leer y generar reporte.

**Lo típico que sale mal (con error real):**
```py
with open("no_existe.txt", "r") as archivo:
    contenido = archivo.read()
```
```
FileNotFoundError: [Errno 2] No such file or directory: 'no_existe.txt'
```
Solución: verifica la ruta o crea el archivo antes de leer.

## Errores típicos y cómo evitarlos
### Error típico: olvidar `\\n` al escribir varias líneas
```py
with open("log.txt", "w") as archivo:
    archivo.write("Evento 1")
    archivo.write("Evento 2")
```

```py
Resultado: "Evento 1Evento 2"
```

Explicación breve: `write()` no agrega saltos de línea. Usa `\\n` para separar.

### Error típico: sobrescribir sin querer
```py
with open("log.txt", "w") as archivo:
    archivo.write("Solo queda este contenido")
```

Explicación breve: el modo `"w"` borra el contenido anterior. Usa `"a"` si quieres agregar.

### Error típico: leer un archivo cerrado
```py
archivo = open("datos.txt", "r")
archivo.close()
archivo.read()
```

```py
ValueError: I/O operation on closed file.
```

Explicación breve: una vez cerrado, debes abrirlo de nuevo.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Leer sin `with` y olvidar cerrar",
                "Si olvidas `close()`, puedes perder datos o bloquear el archivo. Usa `with` siempre que sea posible.",
            ),
            (
                "Abrir con modo incorrecto",
                "Con `\"r\"` no puedes escribir, y con `\"w\"` borras el archivo. Revisa el modo antes de abrir.",
            ),
            (
                "Asumir que el archivo existe",
                "Leer un archivo inexistente lanza `FileNotFoundError`. Verifica rutas o crea el archivo primero.",
            ),
            (
                "Olvidar `\\n` al escribir líneas",
                "Cada `write()` agrega texto sin salto. Añade `\\n` manualmente si lo necesitas.",
            ),
            (
                "Usar `read()` en archivos grandes",
                "`read()` carga todo en memoria. Para archivos grandes, itera línea a línea.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Guardar y cargar un inventario simple",
                """# Aprende esto
# Guardar datos en disco y recuperarlos luego.
# Haz esto
productos = ["teclado", "mouse", "monitor"]

with open("inventario.txt", "w") as archivo:
    for producto in productos:
        archivo.write(producto + "\\n")

recuperados = []
with open("inventario.txt", "r") as archivo:
    for linea in archivo.readlines():
        recuperados.append(linea.strip())

print(recuperados)
# Verás esto
# ['teclado', 'mouse', 'monitor']
# Por qué funciona
# write() guarda cada línea y readlines() recupera el contenido.
""",
            ),
            (
                "Agregar eventos a un log",
                """# Aprende esto
# Agregar información sin borrar lo anterior.
# Haz esto
with open("app.log", "a") as archivo:
    archivo.write("Inicio de sesión\\n")

with open("app.log", "a") as archivo:
    archivo.write("Cierre de sesión\\n")

print("Eventos guardados.")
# Verás esto
# Eventos guardados.
# Por qué funciona
# El modo 'a' agrega al final del archivo.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "title": "Registrar tareas",
                "prompt": (
                    "Crea una lista de 3 tareas y guárdalas en `tareas.txt`, "
                    "una por línea. Luego lee el archivo y muestra la lista "
                    "en pantalla."
                ),
                "solution": (
                    "tareas = ['Leer', 'Practicar', 'Descansar']\n"
                    "with open('tareas.txt', 'w') as archivo:\n"
                    "    for tarea in tareas:\n"
                    "        archivo.write(tarea + '\\n')\n"
                    "\n"
                    "recuperadas = []\n"
                    "with open('tareas.txt', 'r') as archivo:\n"
                    "    for linea in archivo.readlines():\n"
                    "        recuperadas.append(linea.strip())\n"
                    "\n"
                    "print(recuperadas)\n"
                ),
            },
            {
                "title": "Reporte de ventas",
                "prompt": (
                    "Guarda pares `producto,precio` en un archivo `ventas.csv`. "
                    "Luego lee el archivo y muestra solo los productos con precio "
                    "mayor o igual a 100."
                ),
                "solution": (
                    "ventas = ['Silla,120', 'Mesa,80', 'Lampara,150']\n"
                    "with open('ventas.csv', 'w') as archivo:\n"
                    "    for venta in ventas:\n"
                    "        archivo.write(venta + '\\n')\n"
                    "\n"
                    "destacados = []\n"
                    "with open('ventas.csv', 'r') as archivo:\n"
                    "    for linea in archivo.readlines():\n"
                    "        producto, precio = linea.strip().split(',')\n"
                    "        if int(precio) >= 100:\n"
                    "            destacados.append(producto)\n"
                    "\n"
                    "print(destacados)\n"
                ),
            },
        ]

    def build_demo(self) -> QWidget | None:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(
            QLabel(
                "Practica abrir, leer y escribir archivos en un entorno controlado. "
                "Usa `with` para cerrar recursos automáticamente."
            )
        )
        return container

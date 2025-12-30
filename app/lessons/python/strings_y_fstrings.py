from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class StringsFStringsLesson(Lesson):
    TITLE = "Strings y f-strings"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["strings", "f-strings", "format", "texto"]

    def summary(self) -> str:
        return (
            "Domina los textos en Python: creación, concatenación, f-strings, escapes y formato seguro para "
            "mensajes claros y legibles."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: los textos son tu interfaz con el mundo
En Python, los textos (`str`) están en todas partes: mensajes, rutas, nombres y respuestas de una API. Aprender a
manejarlos bien te evita errores de sintaxis y resultados confusos. Recuerda: los strings son inmutables, cada “cambio” crea
uno nuevo.

En esta lección aprenderás desde cero cómo crear textos, unirlos y usar f-strings. Cada concepto incluye un micro-snippet
correcto y un error típico con explicación inmediata.

## Paso 1: crear textos con comillas
Puedes usar comillas simples o dobles. Elige la que haga más legible el texto.

**Así se escribe**
```py
saludo = "Hola"
frase = 'Me gusta Python'
```

**Error típico (❌)**
```py
frase = "Me gusta Python
```

**Qué significa el error**
`SyntaxError` indica que abriste una cadena y no la cerraste.

**Cómo se arregla**
Cierra la comilla o usa el tipo de comilla que no aparezca dentro del texto.

## Paso 2: escapes para comillas y caracteres especiales
Cuando necesitas comillas dentro del texto, usa `\` para escapar.

**Así se escribe**
```py
mensaje = "Ella dijo: \"hola\""
ruta = "C:\\Usuarios\\Ana"
```

**Error típico (❌)**
```py
mensaje = "Ella dijo: "hola""
```

**Qué significa el error**
`SyntaxError` aparece porque las comillas internas cierran el string antes de tiempo.

**Cómo se arregla**
Escapa las comillas internas con `\"` o cambia a comillas simples.

## Paso 3: concatenación básica
Unir textos con `+` es válido, pero debes manejar los espacios.

**Así se escribe**
```py
nombre = "Ana"
mensaje = "Hola " + nombre
```

**Error típico (❌)**
```py
nombre = "Ana"
mensaje = "Hola" + nombre
```

**Qué significa el error**
No hay error de Python, pero el resultado queda pegado: `HolaAna`.

**Cómo se arregla**
Agrega el espacio manualmente o usa una f-string.

## Paso 4: métodos .upper() y .lower()
Estos métodos devuelven un texto nuevo con mayúsculas o minúsculas.

**Así se escribe**
```py
texto = "Hola"
mayus = texto.upper()
```

**Error típico (❌)**
```py
texto = "Hola"
mayus = texto.upper
```

**Qué significa el error**
No obtienes un string, sino una referencia al método. Luego fallará si intentas usarlo como texto.

**Cómo se arregla**
Llama al método con paréntesis: `texto.upper()`.

## Operaciones y métodos más útiles
### Strings (`str`)
1) `upper()` ⭐  
Qué hace: devuelve una versión en mayúsculas.  
Así se escribe:
```py
texto = "hola"
resultado = texto.upper()
```
Error típico:
```py
resultado = texto.upper
```
Verás esto: `"HOLA"`.  
Por qué funciona: los strings son inmutables y el método crea otro texto.  
Lo típico que sale mal: no reasignar el resultado; llamar el método sobre `None`.

2) `lower()` ⭐  
Qué hace: devuelve el texto en minúsculas.  
Así se escribe:
```py
texto = "HoLa"
resultado = texto.lower()
```
Error típico:
```py
resultado = texto.lower
```
Verás esto: `"hola"`.  
Por qué funciona: normaliza el texto para comparar.  
Lo típico que sale mal: creer que cambia el original; comparar sin normalizar ambos lados.

3) `strip()` ⭐  
Qué hace: elimina espacios al inicio y al final.  
Así se escribe:
```py
texto = "  hola  "
resultado = texto.strip()
```
Error típico:
```py
resultado = texto.strip
```
Verás esto: `"hola"`.  
Por qué funciona: recorta whitespace según reglas estándar.  
Lo típico que sale mal: esperar que quite espacios internos; olvidar reasignar.

4) `replace()` ⭐  
Qué hace: reemplaza subcadenas por otra.  
Así se escribe:
```py
texto = "hola mundo"
resultado = texto.replace("mundo", "Python")
```
Error típico:
```py
resultado = texto.replace("mundo")
```
Verás esto: `"hola Python"`.  
Por qué funciona: genera un nuevo texto con el reemplazo.  
Lo típico que sale mal: olvidar el segundo argumento; asumir que modifica el original.

5) `split()` ⭐  
Qué hace: separa el texto en una lista.  
Así se escribe:
```py
texto = "a,b,c"
partes = texto.split(",")
```
Error típico:
```py
partes = texto.split
```
Verás esto: `["a", "b", "c"]`.  
Por qué funciona: divide por el separador y devuelve lista.  
Lo típico que sale mal: confundir split con slicing; usar separador incorrecto.

6) `join()`  
Qué hace: une una lista de textos con un separador.  
Así se escribe:
```py
partes = ["a", "b", "c"]
resultado = ",".join(partes)
```
Error típico:
```py
resultado = partes.join(",")
```
Verás esto: `"a,b,c"`.  
Por qué funciona: `join` es método del separador.  
Lo típico que sale mal: pasar elementos no string; invertir el orden.

7) `startswith()`  
Qué hace: comprueba si empieza con un prefijo.  
Así se escribe:
```py
texto = "admin_01"
es_admin = texto.startswith("admin_")
```
Error típico:
```py
es_admin = texto.startswith["admin_"]
```
Verás esto: `True`.  
Por qué funciona: compara prefijo sin modificar el texto.  
Lo típico que sale mal: usar corchetes; no normalizar mayúsculas/minúsculas.

8) `endswith()`  
Qué hace: comprueba si termina con un sufijo.  
Así se escribe:
```py
archivo = "reporte.csv"
es_csv = archivo.endswith(".csv")
```
Error típico:
```py
es_csv = archivo.endswith(".CSV")
```
Verás esto: `True` o `False` según el texto.  
Por qué funciona: revisa el final de la cadena.  
Lo típico que sale mal: no igualar mayúsculas/minúsculas; asumir que valida el contenido.

9) `format()` / f-string ⭐  
Qué hace: inserta variables en un texto con formato.  
Así se escribe:
```py
nombre = "Ana"
mensaje = f"Hola {nombre}"
```
Error típico:
```py
mensaje = "Hola {nombre}"
```
Verás esto: `"Hola Ana"`.  
Por qué funciona: f-string evalúa expresiones entre llaves.  
Lo típico que sale mal: olvidar la `f`; usar una variable no definida.

## Paso 5: f-strings para insertar variables
Las f-strings son la forma más clara de construir textos con variables.

**Así se escribe**
```py
nombre = "Ana"
edad = 30
mensaje = f"{nombre} tiene {edad} años"
```

**Error típico (❌)**
```py
nombre = "Ana"
mensaje = "{nombre} es cliente"
```

**Qué significa el error**
No hay error de ejecución, pero no se sustituye el valor porque falta la `f`.

**Cómo se arregla**
Agrega la `f` antes de la cadena: `f"{nombre} es cliente"`.

## Paso 6: formato numérico en f-strings
Puedes controlar decimales y relleno con especificadores.

**Así se escribe**
```py
precio = 3.5
mensaje = f"Precio: {precio:.2f}"
```

**Error típico (❌)**
```py
precio = 3.5
mensaje = f"Precio: {precio:2f}"
```

**Qué significa el error**
`ValueError` indica un formato inválido. Los especificadores deben seguir el formato correcto.

**Cómo se arregla**
Usa `:.2f` para dos decimales o revisa la sintaxis del formato.

## Paso 7: resumen para escribir textos confiables
Para textos simples, `+` es suficiente. Para textos con variables, usa f-strings. Para comillas internas, usa escapes o
cambia el tipo de comilla. Con esas reglas evitas la mayoría de errores.



## Micro-ejemplo incremental: sintaxis y errores reales

### Así se escribe
```py
numero = 6
resultado = numero * 2
mensaje = "Doble: " + str(resultado)
print(mensaje)

estado = True
valor = None
if valor is None and estado:
    valor = 0
```

### Error típico: concatenar texto y número
```py
numero = 6
mensaje = "Doble: " + numero
```

```py
TypeError: can only concatenate str (not "int") to str
```

Explicación breve: convierte el número con `str()` o usa f-strings.

### Error típico: operar con texto como número
```py
numero = "6"
resultado = numero / 2
```

```py
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Explicación breve: convierte el texto a `int` o `float` antes de dividir.

### Error típico: operar con None
```py
valor = None
resultado = valor + 1
```

```py
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

Explicación breve: valida `None` con `is None` antes de usarlo.

""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Concatenar texto con número",
                "`\"Total: \" + 10` falla. Convierte el número con `str(10)` o usa f-strings.",
            ),
            (
                "Olvidar espacios en concatenación",
                "Unir `\"Hola\" + \"Mundo\"` produce `HolaMundo`. Agrega el espacio manualmente o usa f-strings.",
            ),
            (
                "Asumir que upper() modifica el texto",
                "Los strings son inmutables. `texto.upper()` devuelve uno nuevo; si no lo reasignas, no cambia.",
            ),
            (
                "Olvidar paréntesis en un método",
                "`texto.upper` no ejecuta el método. Debes escribir `texto.upper()` para obtener el resultado.",
            ),
            (
                "Escapar comillas incorrectamente",
                "Si usas comillas dobles dentro de un texto con dobles, debes escaparlas o cambiar de comillas.",
            ),
            (
                "Mezclar \n con triple comilla sin intención",
                "Cuando mezclas ambos puedes obtener saltos de línea duplicados. Elige un método consistente.",
            ),
            (
                "Formatear decimales sin redondear",
                "Mostrar un float sin formato puede dar muchos decimales. Usa `{valor:.2f}` para control.",
            ),
            (
                "Olvidar la f en una f-string",
                "`\"{nombre}\"` no sustituye la variable. Agrega la `f` al inicio.",
            ),
            (
                "Usar llaves sin variable",
                "`f\"{}\"` es un `SyntaxError`. Dentro de `{}` debe ir una expresión válida.",
            ),
            (
                "Confundir comillas en textos largos",
                "Si abres con triple comilla, debes cerrar con triple comilla del mismo tipo.",
            ),
            (
                "Rutas de Windows sin escapar",
                "`\"C:\\\\nueva\"` interpreta `\\n` como salto de línea. Usa `\\\\` o raw strings.",
            ),
            (
                "Concatenar demasiados fragmentos",
                "Si hay varias variables, la concatenación se vuelve ilegible. Prefiere f-strings.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear strings con comillas",
                """# Aprende esto
# Aprenderás a crear textos con comillas simples y dobles.
# Verás cómo combinar comillas sin escapes extra.
# Entenderás cuándo cambiar el tipo de comilla.
#
# Haz esto
saludo = "Hola"  # Texto con comillas dobles
respuesta = 'Estoy bien'  # Texto con comillas simples
mensaje = saludo + ", " + respuesta  # Unimos textos
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Hola, Estoy bien".
#
# Por qué funciona
# Ambos valores son strings y se concatenan con +.
#
# Lo típico que sale mal
# - Olvidar cerrar comillas y tener SyntaxError.
# - Mezclar comillas sin control y romper el texto.
""",
            ),
            (
                "Escapes en textos",
                """# Aprende esto
# Aprenderás a escapar comillas y barras.
# Verás cómo escribir rutas y citas.
# Entenderás el uso de \\.
#
# Haz esto
cita = "Ella dijo: \"hola\""  # Escapamos comillas
ruta = "C:\\Usuarios\\Ana"  # Escapamos barras
print(cita)  # Mostramos la cita
print(ruta)  # Mostramos la ruta
#
# Verás esto
# Verás la cita con comillas y la ruta completa.
#
# Por qué funciona
# El escape evita que las comillas cierren el string.
#
# Lo típico que sale mal
# - Escribir comillas internas sin escape.
# - Olvidar duplicar las barras en rutas.
""",
            ),
            (
                "Concatenación clara",
                """# Aprende esto
# Aprenderás a concatenar strings con espacios controlados.
# Verás cómo evitar textos pegados.
# Entenderás cuándo pasar a f-strings.
#
# Haz esto
nombre = "Ana"  # Guardamos el nombre
saludo = "Hola " + nombre  # Unimos con espacio
pregunta = "¿Cómo estás?"  # Texto adicional
mensaje = saludo + ". " + pregunta  # Texto final
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Hola Ana. ¿Cómo estás?".
#
# Por qué funciona
# La concatenación respeta los espacios manuales.
#
# Lo típico que sale mal
# - Olvidar el espacio y obtener "HolaAna".
# - Encadenar demasiados + y perder legibilidad.
""",
            ),
            (
                "upper y lower en acción",
                """# Aprende esto
# Aprenderás a transformar textos con upper y lower.
# Verás que el resultado es un string nuevo.
# Entenderás la necesidad de reasignar.
#
# Haz esto
texto = "Python"  # Texto original
mayus = texto.upper()  # Pasamos a mayúsculas
minus = texto.lower()  # Pasamos a minúsculas
print(mayus)  # Mostramos mayúsculas
print(minus)  # Mostramos minúsculas
#
# Verás esto
# Verás "PYTHON" y "python".
#
# Por qué funciona
# upper y lower devuelven strings nuevos.
#
# Lo típico que sale mal
# - Escribir texto.upper sin paréntesis.
# - Asumir que el texto original cambia.
""",
            ),
            (
                "F-strings básicos",
                """# Aprende esto
# Aprenderás a insertar variables con f-strings.
# Verás la frase completa de una vez.
# Entenderás la legibilidad del formato.
#
# Haz esto
nombre = "Ana"  # Guardamos el nombre
edad = 30  # Guardamos la edad
mensaje = f"{nombre} tiene {edad} años"  # Texto con variables
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Ana tiene 30 años".
#
# Por qué funciona
# La f-string sustituye los valores dentro de {}.
#
# Lo típico que sale mal
# - Olvidar la f y ver {nombre} literal.
# - Usar llaves vacías y provocar SyntaxError.
""",
            ),
            (
                "Formato numérico en f-strings",
                """# Aprende esto
# Aprenderás a controlar decimales.
# Verás cómo dar formato de salida.
# Entenderás la sintaxis de :.2f.
#
# Haz esto
precio = 3.5  # Precio base
impuesto = 0.21  # Impuesto
final = precio * (1 + impuesto)  # Precio final
mensaje = f"Precio final: {final:.2f} €"  # Dos decimales
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Precio final: 4.24 €".
#
# Por qué funciona
# :.2f redondea a dos decimales.
#
# Lo típico que sale mal
# - Usar un especificador inválido y fallar.
# - Mostrar floats sin formato y obtener ruido.
""",
            ),
            (
                "Multilínea con \n",
                """# Aprende esto
# Aprenderás a construir textos con saltos de línea.
# Verás cómo aparece cada línea en pantalla.
# Entenderás cuándo usar \n.
#
# Haz esto
linea1 = "Línea 1"  # Primera línea
linea2 = "Línea 2"  # Segunda línea
mensaje = linea1 + "\n" + linea2  # Unimos con salto
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás dos líneas separadas en pantalla.
#
# Por qué funciona
# \n inserta un salto de línea dentro del string.
#
# Lo típico que sale mal
# - Escribir /n y no obtener salto.
# - Mezclar \n y triple comilla sin intención.
""",
            ),
            (
                "Triple comilla para plantillas",
                """# Aprende esto
# Aprenderás a crear textos largos con triple comilla.
# Verás cómo respetar la forma original.
# Entenderás su uso en plantillas.
#
# Haz esto
plantilla = """Hola {nombre}
Gracias por tu compra.
Saludos."""  # Plantilla multilínea
print(plantilla)  # Mostramos la plantilla
#
# Verás esto
# Verás el texto en varias líneas.
#
# Por qué funciona
# La triple comilla conserva saltos de línea.
#
# Lo típico que sale mal
# - No cerrar la triple comilla y tener SyntaxError.
# - Mezclar comillas simples y dobles sin control.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un string con tu nombre y muestra un saludo usando concatenación.",
                "hints": ["Usa + para unir textos.", "Incluye un espacio en el saludo."],
                "solution": """nombre = "Ana"
saludo = "Hola " + nombre
print(saludo)""",
            },
            {
                "question": "Escribe una frase que incluya comillas dobles dentro del texto.",
                "hints": ["Usa escape con \\\".", "También puedes usar comillas simples afuera."],
                "solution": """frase = "Ella dijo: \"hola\""
print(frase)""",
            },
            {
                "question": "Convierte un texto a mayúsculas usando upper() y guárdalo en otra variable.",
                "hints": ["No olvides los paréntesis.", "Reasigna el resultado."],
                "solution": """texto = "Python"
mayus = texto.upper()
print(mayus)""",
            },
            {
                "question": "Crea una f-string que muestre el precio con dos decimales.",
                "hints": ["Usa {precio:.2f}.", "Recuerda la f al inicio."],
                "solution": """precio = 9.5
mensaje = f"Precio: {precio:.2f}"
print(mensaje)""",
            },
            {
                "question": "Construye un texto de dos líneas usando \n.",
                "hints": ["Une las líneas con +.", "Usa \\n entre ellas."],
                "solution": """linea1 = "Hola"
linea2 = "Mundo"
mensaje = linea1 + "\n" + linea2
print(mensaje)""",
            },
            {
                "question": "Crea una f-string que inserte nombre y edad.",
                "hints": ["Usa {nombre} y {edad}.", "Define ambas variables antes."],
                "solution": """nombre = "Ana"
edad = 30
mensaje = f"{nombre} tiene {edad} años"
print(mensaje)""",
            },
        ]

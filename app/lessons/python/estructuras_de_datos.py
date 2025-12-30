from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class EstructurasDatosLesson(Lesson):
    TITLE = "Estructuras de datos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["listas", "diccionarios", "colecciones", "datos"]

    def summary(self) -> str:
        return (
            "Aprende a usar listas y diccionarios desde cero: cómo crear, acceder, agregar elementos y "
            "evitar errores típicos como IndexError o KeyError."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: guardar colecciones de datos
Cuando tienes más de un dato relacionado, necesitas una estructura para guardarlos juntos. Las listas guardan elementos
ordenados; los diccionarios guardan pares clave-valor. Ambos son fundamentales en Python.

En esta lección aprenderás la sintaxis básica con micro-snippets correctos e incorrectos.

## Paso 1: listas con []
Las listas se crean con corchetes y pueden contener varios elementos.

**Así se escribe**
```py
frutas = ["manzana", "pera", "uva"]
```

**Error típico (❌)**
```py
frutas = ("manzana", "pera", "uva")
```

**Qué significa el error**
No es un error de Python, pero has creado una tupla, no una lista. Las tuplas no se modifican.

**Cómo se arregla**
Usa corchetes `[]` cuando necesites una lista mutable.

## Paso 2: agregar con append
`append` agrega un elemento al final de la lista.

**Así se escribe**
```py
frutas = ["manzana", "pera"]
frutas.append("uva")
```

**Error típico (❌)**
```py
frutas = ["manzana", "pera"]
frutas.append["uva"]
```

**Qué significa el error**
`TypeError` porque `append` es un método y debe llamarse con paréntesis.

**Cómo se arregla**
Usa `frutas.append("uva")` con paréntesis.

## Paso 3: indexar elementos
Accedes a un elemento con índices desde 0.

**Así se escribe**
```py
frutas = ["manzana", "pera"]
primera = frutas[0]
```

**Error típico (❌)**
```py
frutas = ["manzana", "pera"]
tercera = frutas[2]
```

**Qué significa el error**
`IndexError` indica que el índice está fuera de rango.

**Cómo se arregla**
Usa índices válidos y revisa `len(frutas)`.

## Paso 4: diccionarios con {}
Los diccionarios guardan pares clave-valor.

**Así se escribe**
```py
persona = {"nombre": "Ana", "edad": 30}
```

**Error típico (❌)**
```py
persona = {"nombre", "Ana"}
```

**Qué significa el error**
No es un diccionario, es un conjunto (`set`). Falta el `:` entre clave y valor.

**Cómo se arregla**
Escribe `clave: valor` dentro de `{}`.

## Paso 5: acceder por clave y usar get
Accede a valores con `diccionario[clave]`. Si la clave no existe, puedes usar `.get()`.

**Así se escribe**
```py
persona = {"nombre": "Ana", "edad": 30}
edad = persona["edad"]
ciudad = persona.get("ciudad", "Desconocida")
```

**Error típico (❌)**
```py
persona = {"nombre": "Ana"}
edad = persona["edad"]
```

**Qué significa el error**
`KeyError` aparece porque la clave no existe.

**Cómo se arregla**
Verifica que la clave exista o usa `get` con un valor por defecto.

## Paso 6: resumen para usar estructuras sin errores
Recuerda: listas con `[]` e índices desde 0; diccionarios con `{}` y claves explícitas. Usa `append` con paréntesis y `get`
para evitar errores por claves faltantes.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir lista con tupla",
                "`(1, 2)` crea una tupla. Usa `[]` si necesitas modificarla.",
            ),
            (
                "Olvidar paréntesis en append",
                "`append` es un método. Sin paréntesis obtienes un error de tipo.",
            ),
            (
                "IndexError por índice fuera de rango",
                "Acceder a `lista[3]` cuando solo hay 3 elementos falla. Usa `len` para validar.",
            ),
            (
                "Confundir dict con set",
                "`{""a"", ""b""}` crea un set. Un diccionario necesita `:`.",
            ),
            (
                "KeyError por clave inexistente",
                "Si la clave no existe, usar `diccionario[clave]` falla. Usa `.get`.",
            ),
            (
                "Modificar una lista mientras iteras",
                "Puedes saltarte elementos. Crea una copia si necesitas modificar.",
            ),
            (
                "Usar índices negativos sin querer",
                "`lista[-1]` da el último elemento. Asegúrate de querer ese comportamiento.",
            ),
            (
                "Asumir orden en diccionarios antiguos",
                "En versiones muy antiguas el orden no estaba garantizado. Evita depender de él.",
            ),
            (
                "Guardar tipos mezclados sin intención",
                "Mezclar int y str en una lista sin motivo puede complicar el procesamiento.",
            ),
            (
                "No manejar listas vacías",
                "Acceder a índice 0 en una lista vacía siempre falla.",
            ),
            (
                "Reutilizar claves en dict",
                "Si repites una clave, se sobrescribe el valor anterior.",
            ),
            (
                "Confundir copy con copia profunda",
                "`copy()` en listas solo copia el primer nivel.",
            ),
            (
                "No usar get con valor por defecto",
                "Si esperas una clave opcional, usa `.get(""clave"", valor)`.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear una lista",
                """# Aprende esto
# Aprenderás a crear una lista con corchetes.
# Verás varios elementos en orden.
# Entenderás cómo se guarda la colección.
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista de frutas
print(frutas)  # Mostramos la lista
#
# Verás esto
# Verás ['manzana', 'pera', 'uva'].
#
# Por qué funciona
# Los corchetes definen una lista mutable.
#
# Lo típico que sale mal
# - Usar paréntesis y crear una tupla.
# - Olvidar las comas entre elementos.
""",
            ),
            (
                "Append en listas",
                """# Aprende esto
# Aprenderás a añadir elementos con append.
# Verás cómo crece la lista.
# Entenderás que append modifica en sitio.
#
# Haz esto
frutas = ["manzana", "pera"]  # Lista inicial
frutas.append("uva")  # Agregamos una fruta
print(frutas)  # Mostramos la lista
#
# Verás esto
# Verás ['manzana', 'pera', 'uva'].
#
# Por qué funciona
# append agrega al final sin crear otra lista.
#
# Lo típico que sale mal
# - Escribir append con corchetes.
# - Esperar que append devuelva una lista nueva.
""",
            ),
            (
                "Acceso por índice",
                """# Aprende esto
# Aprenderás a acceder a elementos por índice.
# Verás que el índice empieza en 0.
# Entenderás el uso de len.
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista
primera = frutas[0]  # Primer elemento
ultima = frutas[-1]  # Último elemento
print(primera)  # Mostramos
print(ultima)  # Mostramos
#
# Verás esto
# Verás "manzana" y "uva".
#
# Por qué funciona
# Los índices positivos y negativos apuntan a posiciones válidas.
#
# Lo típico que sale mal
# - Usar un índice fuera de rango.
# - Olvidar que el índice empieza en 0.
""",
            ),
            (
                "Modificar una lista",
                """# Aprende esto
# Aprenderás a reemplazar un elemento.
# Verás cómo cambia la lista en sitio.
# Entenderás la mutabilidad.
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista
frutas[1] = "kiwi"  # Reemplazamos
print(frutas)  # Mostramos
#
# Verás esto
# Verás ['manzana', 'kiwi', 'uva'].
#
# Por qué funciona
# Las listas son mutables y admiten asignación por índice.
#
# Lo típico que sale mal
# - Usar un índice fuera de rango.
# - Esperar que las tuplas permitan esto.
""",
            ),
            (
                "Crear un diccionario",
                """# Aprende esto
# Aprenderás a crear un diccionario con claves.
# Verás pares clave-valor.
# Entenderás la sintaxis con :.
#
# Haz esto
persona = {"nombre": "Ana", "edad": 30}  # Diccionario
print(persona)  # Mostramos
#
# Verás esto
# Verás {'nombre': 'Ana', 'edad': 30}.
#
# Por qué funciona
# Cada clave tiene asociado un valor.
#
# Lo típico que sale mal
# - Olvidar el : y crear un set.
# - Repetir claves y sobrescribir valores.
""",
            ),
            (
                "Acceso por clave",
                """# Aprende esto
# Aprenderás a leer valores por clave.
# Verás cómo usar un diccionario real.
# Entenderás la lectura directa.
#
# Haz esto
persona = {"nombre": "Ana", "edad": 30}  # Diccionario
nombre = persona["nombre"]  # Accedemos a la clave
print(nombre)  # Mostramos
#
# Verás esto
# Verás "Ana".
#
# Por qué funciona
# La clave existe y devuelve su valor asociado.
#
# Lo típico que sale mal
# - Usar una clave inexistente y tener KeyError.
# - Usar el nombre de la clave sin comillas.
""",
            ),
            (
                "Acceso seguro con get",
                """# Aprende esto
# Aprenderás a evitar KeyError con get.
# Verás un valor por defecto.
# Entenderás la seguridad del acceso.
#
# Haz esto
persona = {"nombre": "Ana", "edad": 30}  # Diccionario
ciudad = persona.get("ciudad", "Desconocida")  # Valor seguro
print(ciudad)  # Mostramos
#
# Verás esto
# Verás "Desconocida".
#
# Por qué funciona
# get devuelve un valor por defecto si la clave falta.
#
# Lo típico que sale mal
# - Usar persona["ciudad"] y lanzar KeyError.
# - Olvidar el valor por defecto.
""",
            ),
            (
                "Recorrer un diccionario",
                """# Aprende esto
# Aprenderás a recorrer claves y valores.
# Verás cómo imprimirlos juntos.
# Entenderás items().
#
# Haz esto
persona = {"nombre": "Ana", "edad": 30}  # Diccionario
for clave, valor in persona.items():  # Recorremos pares
    print(clave, valor)  # Mostramos
#
# Verás esto
# Verás "nombre Ana" y "edad 30".
#
# Por qué funciona
# items() devuelve pares clave-valor.
#
# Lo típico que sale mal
# - Iterar solo claves y olvidar los valores.
# - Modificar el diccionario mientras iteras.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una lista con tres números y muestra el primero.",
                "hints": ["Usa corchetes.", "El primer índice es 0."],
                "solution": """numeros = [1, 2, 3]
print(numeros[0])""",
            },
            {
                "question": "Agrega un elemento al final de una lista usando append().",
                "hints": ["append lleva paréntesis.", "Modifica la lista en sitio."],
                "solution": """frutas = ["manzana", "pera"]
frutas.append("uva")
print(frutas)""",
            },
            {
                "question": "Reemplaza el segundo elemento de una lista por otro valor.",
                "hints": ["Usa índice 1.", "Asigna con =."],
                "solution": """colores = ["rojo", "verde", "azul"]
colores[1] = "negro"
print(colores)""",
            },
            {
                "question": "Crea un diccionario con nombre y edad, luego imprime la edad.",
                "hints": ["Usa clave: valor.", "Accede con diccionario[\"edad\"]."],
                "solution": """persona = {"nombre": "Ana", "edad": 30}
print(persona["edad"])""",
            },
            {
                "question": "Accede a una clave que puede faltar usando get con valor por defecto.",
                "hints": ["Usa .get(\"clave\", \"valor\").", "Imprime el resultado."],
                "solution": """persona = {"nombre": "Ana"}
ciudad = persona.get("ciudad", "Desconocida")
print(ciudad)""",
            },
            {
                "question": "Recorre un diccionario y muestra clave y valor en cada línea.",
                "hints": ["Usa items().", "Desempaqueta clave y valor."],
                "solution": """persona = {"nombre": "Ana", "edad": 30}
for clave, valor in persona.items():
    print(clave, valor)""",
            },
        ]

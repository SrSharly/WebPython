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

## Operaciones y métodos más útiles
### Listas (`list`)
1) `append()` ⭐  
Qué hace: agrega al final.  
Así se escribe:
```py
frutas = ["manzana"]
frutas.append("pera")
```
Error típico:
```py
frutas.append["pera"]
```
Verás esto: `["manzana", "pera"]`.  
Por qué funciona: `append` muta la lista.  
Lo típico que sale mal: olvidar paréntesis; pensar que devuelve una nueva lista.

2) `extend()` ⭐  
Qué hace: añade varios elementos.  
Así se escribe:
```py
frutas = ["manzana"]
frutas.extend(["pera", "uva"])
```
Error típico:
```py
frutas.extend("uva")
```
Verás esto: `["manzana", "pera", "uva"]`.  
Por qué funciona: recorre el iterable.  
Lo típico que sale mal: pasar string y separar por letras; confundir con `append`.

3) `insert()`  
Qué hace: inserta en índice.  
Así se escribe:
```py
frutas = ["manzana", "uva"]
frutas.insert(1, "pera")
```
Error típico:
```py
frutas.insert("1", "pera")
```
Verás esto: `["manzana", "pera", "uva"]`.  
Por qué funciona: usa índice entero.  
Lo típico que sale mal: índice fuera de rango; usar índice string.

4) `pop()` ⭐  
Qué hace: quita y devuelve elemento.  
Así se escribe:
```py
frutas = ["manzana", "pera"]
ultima = frutas.pop()
```
Error típico:
```py
frutas.pop(5)
```
Verás esto: `ultima = "pera"`.  
Por qué funciona: elimina el elemento y lo retorna.  
Lo típico que sale mal: `IndexError`; mutar durante iteración.

5) `remove()`  
Qué hace: elimina por valor.  
Así se escribe:
```py
frutas = ["manzana", "pera"]
frutas.remove("pera")
```
Error típico:
```py
frutas.remove("uva")
```
Verás esto: `["manzana"]`.  
Por qué funciona: busca el valor y lo borra.  
Lo típico que sale mal: `ValueError` si no existe; duplicados inesperados.

6) `sort()` ⭐  
Qué hace: ordena la lista.  
Así se escribe:
```py
numeros = [3, 1, 2]
numeros.sort()
```
Error típico:
```py
ordenados = numeros.sort()
```
Verás esto: `[1, 2, 3]`.  
Por qué funciona: ordena en sitio y devuelve `None`.  
Lo típico que sale mal: esperar nueva lista; mezclar tipos incompatibles.

7) `len()` ⭐  
Qué hace: cuenta elementos.  
Así se escribe:
```py
frutas = ["manzana", "pera"]
total = len(frutas)
```
Error típico:
```py
total = frutas.len()
```
Verás esto: `2`.  
Por qué funciona: `len()` es función global.  
Lo típico que sale mal: usar `.len()`; olvidar validar antes de indexar.

### Diccionarios (`dict`)
1) `get()` ⭐  
Qué hace: lee sin `KeyError`.  
Así se escribe:
```py
persona = {"nombre": "Ana"}
ciudad = persona.get("ciudad", "Desconocida")
```
Error típico:
```py
ciudad = persona["ciudad"]
```
Verás esto: `"Desconocida"`.  
Por qué funciona: devuelve valor por defecto.  
Lo típico que sale mal: olvidar default; confiar en claves que no existen.

2) `keys()`  
Qué hace: devuelve las claves.  
Así se escribe:
```py
persona = {"nombre": "Ana"}
claves = list(persona.keys())
```
Error típico:
```py
claves = persona.keys
```
Verás esto: `["nombre"]`.  
Por qué funciona: `keys()` crea una vista.  
Lo típico que sale mal: olvidar paréntesis; asumir lista.

3) `values()`  
Qué hace: devuelve los valores.  
Así se escribe:
```py
persona = {"nombre": "Ana"}
valores = list(persona.values())
```
Error típico:
```py
valores = persona.values
```
Verás esto: `["Ana"]`.  
Por qué funciona: devuelve vista de valores.  
Lo típico que sale mal: olvidar paréntesis; mutar dict mientras iteras.

4) `items()` ⭐  
Qué hace: pares clave-valor.  
Así se escribe:
```py
persona = {"nombre": "Ana"}
pares = list(persona.items())
```
Error típico:
```py
pares = persona.items
```
Verás esto: `[("nombre", "Ana")]`.  
Por qué funciona: expone pares.  
Lo típico que sale mal: olvidar paréntesis; modificar dict durante iteración.

5) `update()` ⭐  
Qué hace: mezcla otro dict.  
Así se escribe:
```py
persona = {"nombre": "Ana"}
persona.update({"edad": 30})
```
Error típico:
```py
persona.update("edad")
```
Verás esto: `{"nombre": "Ana", "edad": 30}`.  
Por qué funciona: actualiza claves existentes o nuevas.  
Lo típico que sale mal: pasar string; sobrescribir claves sin querer.

6) `pop()`  
Qué hace: elimina y devuelve una clave.  
Así se escribe:
```py
persona = {"nombre": "Ana"}
nombre = persona.pop("nombre")
```
Error típico:
```py
persona.pop("edad")
```
Verás esto: `"Ana"`.  
Por qué funciona: quita la clave y retorna su valor.  
Lo típico que sale mal: `KeyError` si falta; eliminar claves necesarias.

7) `setdefault()`  
Qué hace: obtiene o crea clave.  
Así se escribe:
```py
persona = {}
persona.setdefault("rol", "cliente")
```
Error típico:
```py
persona.setdefault()
```
Verás esto: `{"rol": "cliente"}`.  
Por qué funciona: crea si no existe.  
Lo típico que sale mal: usarlo para actualizar siempre; olvidar el valor por defecto.

8) `len()` ⭐  
Qué hace: cuenta claves.  
Así se escribe:
```py
persona = {"nombre": "Ana"}
total = len(persona)
```
Error típico:
```py
total = persona.len()
```
Verás esto: `1`.  
Por qué funciona: `len()` cuenta entradas.  
Lo típico que sale mal: usar `.len()`; asumir que cuenta valores únicos.

### Tuplas (`tuple`)
1) `count()`  
Qué hace: cuenta ocurrencias.  
Así se escribe:
```py
coords = (1, 2, 1)
total = coords.count(1)
```
Error típico:
```py
total = coords.count[1]
```
Verás esto: `2`.  
Por qué funciona: busca el valor en la tupla.  
Lo típico que sale mal: usar corchetes; confundir con `len`.

2) `index()`  
Qué hace: devuelve la posición de un valor.  
Así se escribe:
```py
coords = (1, 2, 3)
pos = coords.index(2)
```
Error típico:
```py
pos = coords.index(5)
```
Verás esto: `1`.  
Por qué funciona: busca el primer índice.  
Lo típico que sale mal: `ValueError` si no existe; pensar que devuelve todos los índices.

3) `len()` ⭐  
Qué hace: cuenta elementos.  
Así se escribe:
```py
coords = (1, 2, 3)
total = len(coords)
```
Error típico:
```py
total = coords.len()
```
Verás esto: `3`.  
Por qué funciona: `len()` funciona con tuplas.  
Lo típico que sale mal: usar `.len()`; olvidar que es inmutable.

4) `in` ⭐  
Qué hace: comprueba pertenencia.  
Así se escribe:
```py
coords = (1, 2, 3)
existe = 2 in coords
```
Error típico:
```py
existe = coords in 2
```
Verás esto: `True`.  
Por qué funciona: `in` busca en la tupla.  
Lo típico que sale mal: invertir el orden; esperar index de retorno.

5) slicing  
Qué hace: extrae porciones.  
Así se escribe:
```py
coords = (1, 2, 3, 4)
segmento = coords[1:3]
```
Error típico:
```py
segmento = coords[1, 3]
```
Verás esto: `(2, 3)`.  
Por qué funciona: slicing crea una tupla nueva.  
Lo típico que sale mal: usar coma en lugar de `:`; pensar que modifica en sitio.

6) unpacking  
Qué hace: asigna elementos a variables.  
Así se escribe:
```py
coords = (1, 2)
x, y = coords
```
Error típico:
```py
x, y, z = coords
```
Verás esto: `x = 1`, `y = 2`.  
Por qué funciona: las cantidades deben coincidir.  
Lo típico que sale mal: desempaquetar con distinto número; olvidar usar `_` para ignorar.

### Conjuntos (`set`)
1) `add()` ⭐  
Qué hace: agrega un elemento.  
Así se escribe:
```py
colores = {"rojo"}
colores.add("azul")
```
Error típico:
```py
colores.add(["azul"])
```
Verás esto: `{"rojo", "azul"}`.  
Por qué funciona: agrega elementos únicos.  
Lo típico que sale mal: usar listas (no hashables); esperar orden.

2) `update()`  
Qué hace: agrega varios elementos.  
Así se escribe:
```py
colores = {"rojo"}
colores.update(["azul", "verde"])
```
Error típico:
```py
colores.update("azul")
```
Verás esto: `{"rojo", "azul", "verde"}`.  
Por qué funciona: agrega cada elemento del iterable.  
Lo típico que sale mal: pasar string y separar por letras; olvidar que no hay orden.

3) `remove()` / `discard()` ⭐  
Qué hace: elimina un elemento.  
Así se escribe:
```py
colores = {"rojo", "azul"}
colores.discard("rojo")
```
Error típico:
```py
colores.remove("verde")
```
Verás esto: `{"azul"}`.  
Por qué funciona: `discard` no falla si no existe.  
Lo típico que sale mal: `KeyError` con `remove`; asumir orden.

4) `union()`  
Qué hace: une conjuntos.  
Así se escribe:
```py
a = {1, 2}
b = {2, 3}
resultado = a.union(b)
```
Error típico:
```py
resultado = a + b
```
Verás esto: `{1, 2, 3}`.  
Por qué funciona: `union` combina elementos únicos.  
Lo típico que sale mal: usar `+`; olvidar que devuelve un set nuevo.

5) `intersection()`  
Qué hace: elementos comunes.  
Así se escribe:
```py
a = {1, 2}
b = {2, 3}
resultado = a.intersection(b)
```
Error típico:
```py
resultado = a.intersection()
```
Verás esto: `{2}`.  
Por qué funciona: cruza ambos sets.  
Lo típico que sale mal: olvidar el otro set; confundir con diferencia.

6) `difference()`  
Qué hace: resta elementos.  
Así se escribe:
```py
a = {1, 2, 3}
b = {2}
resultado = a.difference(b)
```
Error típico:
```py
resultado = a.difference()
```
Verás esto: `{1, 3}`.  
Por qué funciona: quita los del otro set.  
Lo típico que sale mal: olvidar el argumento; suponer orden.

7) `len()` ⭐  
Qué hace: cuenta elementos únicos.  
Así se escribe:
```py
colores = {"rojo", "azul"}
total = len(colores)
```
Error típico:
```py
total = colores.len()
```
Verás esto: `2`.  
Por qué funciona: cuenta elementos del set.  
Lo típico que sale mal: usar `.len()`; asumir que el orden es estable.

## Paso 6: resumen para usar estructuras sin errores
Recuerda: listas con `[]` e índices desde 0; diccionarios con `{}` y claves explícitas. Usa `append` con paréntesis y `get`
para evitar errores por claves faltantes.



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

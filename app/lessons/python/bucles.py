from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class BuclesLesson(Lesson):
    TITLE = "Bucles"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["bucles", "for", "while", "range", "break", "continue"]

    def summary(self) -> str:
        return (
            "Aprende a repetir tareas con for y while, controlar ciclos con break/continue y evitar "
            "bucles infinitos o errores de rango."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: repetir sin duplicar
Los bucles te permiten repetir acciones sin escribir la misma línea muchas veces. En Python los dos principales son `for` y
`while`. Cada uno tiene su forma y sus errores típicos.

En esta lección aprenderás la sintaxis básica con micro-snippets correctos e incorrectos, justo en el momento en que se
presenta cada concepto.

## Paso 1: for con range
`for` recorre una secuencia. `range(n)` genera números desde 0 hasta n-1.

**Así se escribe**
```py
for i in range(3):
    print(i)
```

**Error típico (❌)**
```py
for i in range(3)
    print(i)
```

**Qué significa el error**
`SyntaxError` porque falta el `:` al final de la línea del `for`.

**Cómo se arregla**
Agrega `:` y mantén la indentación del bloque.

## Paso 2: while con condición
`while` repite mientras una condición sea True. Necesitas actualizar la variable para evitar bucles infinitos.

**Así se escribe**
```py
contador = 0
while contador < 3:
    print(contador)
    contador += 1
```

**Error típico (❌)**
```py
contador = 0
while contador < 3:
    print(contador)
```

**Qué significa el error**
No hay error de sintaxis, pero el bucle se vuelve infinito porque `contador` nunca cambia.

**Cómo se arregla**
Actualiza la variable dentro del bucle: `contador += 1`.

### Así se escribe: while con input y conversión
```py
intentos = 0
limite = int(input("¿Cuántos intentos? "))
while intentos < limite:
    print("Intento", intentos)
    intentos += 1
```

### Error típico: comparar input sin convertir
```py
limite = input("¿Cuántos intentos? ")
intentos = 0
while intentos < limite:
    intentos += 1
```

```py
TypeError: '<' not supported between instances of 'int' and 'str'
```

Explicación breve: `input()` devuelve `str`, así que debes convertir con `int()` antes de comparar.

## Paso 3: break para salir
`break` corta el bucle cuando se cumple una condición específica.

**Así se escribe**
```py
for numero in range(5):
    if numero == 3:
        break
    print(numero)
```

**Error típico (❌)**
```py
for numero in range(5):
    if numero == 3:
    break
```

**Qué significa el error**
`IndentationError` porque `break` debe estar indentado dentro del `if`.

**Cómo se arregla**
Indenta `break` al mismo nivel que el bloque del `if`.

## Paso 4: continue para saltar
`continue` salta a la siguiente iteración sin ejecutar el resto del bloque.

**Así se escribe**
```py
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
```

**Error típico (❌)**
```py
for numero in range(5):
    if numero == 2:
        continue
        print(numero)
```

**Qué significa el error**
No hay error de sintaxis, pero `print` nunca se ejecuta en ese bloque porque `continue` lo salta.

**Cómo se arregla**
Coloca `continue` antes de lo que quieres omitir y el resto fuera del bloque o después del `if`.

## Paso 5: resumen para bucles seguros
Usa `for` con `range` para conteos y `while` para condiciones abiertas. En `while`, actualiza la variable siempre. Usa
`break` y `continue` con cuidado y buena indentación.



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
                "Olvidar el : en for o while",
                "`for i in range(3)` sin `:` produce `SyntaxError`.",
            ),
            (
                "No actualizar la variable en while",
                "El bucle se vuelve infinito si la condición nunca cambia.",
            ),
            (
                "Usar range con límite incorrecto",
                "`range(3)` genera 0,1,2. Si esperas 3, ajusta el límite.",
            ),
            (
                "Olvidar la indentación",
                "`IndentationError` ocurre si el bloque no está indentado.",
            ),
            (
                "Usar break fuera de un bucle",
                "`SyntaxError` si `break` está fuera de un `for` o `while`.",
            ),
            (
                "Usar continue sin lógica",
                "Si `continue` está al inicio, puedes saltarte todo el trabajo del bucle.",
            ),
            (
                "Modificar la lista que recorres",
                "Cambiar la lista mientras iteras puede saltar elementos o duplicar resultados.",
            ),
            (
                "Olvidar inicializar contador",
                "En `while`, si no inicializas, tendrás `NameError`.",
            ),
            (
                "Confundir range con índices",
                "`range(len(lista))` da índices, no valores. Usa `for item in lista` cuando puedas.",
            ),
            (
                "Usar else en loops sin entender",
                "El else de un bucle se ejecuta si no hay break. Puede sorprender.",
            ),
            (
                "Imprimir dentro del bucle sin control",
                "Demasiadas impresiones hacen difícil leer la salida. Usa contadores o condiciones.",
            ),
            (
                "Comparar strings en while",
                "Cuidado con mayúsculas/minúsculas. Normaliza antes de comparar.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "For con range",
                """# Aprende esto
# Aprenderás a repetir con range.
# Verás cómo contar desde cero.
# Entenderás la salida por iteración.
#
# Haz esto
for i in range(3):  # Recorremos 0,1,2
    print(i)  # Mostramos i
#
# Verás esto
# Verás 0, 1, 2 en líneas separadas.
#
# Por qué funciona
# range(3) genera tres valores consecutivos.
#
# Lo típico que sale mal
# - Olvidar el : en el for.
# - Esperar que llegue hasta 3 incluido.
""",
            ),
            (
                "For con lista",
                """# Aprende esto
# Aprenderás a recorrer una lista.
# Verás valores en cada iteración.
# Entenderás la ventaja de iterar directo.
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista
for fruta in frutas:  # Recorremos valores
    print(fruta)  # Mostramos cada fruta
#
# Verás esto
# Verás cada fruta en su propia línea.
#
# Por qué funciona
# El for toma cada elemento de la lista.
#
# Lo típico que sale mal
# - Modificar la lista mientras iteras.
# - Usar índices cuando no hace falta.
""",
            ),
            (
                "While con contador",
                """# Aprende esto
# Aprenderás a usar while con contador.
# Verás la condición que se actualiza.
# Entenderás cómo evitar bucles infinitos.
#
# Haz esto
contador = 0  # Inicializamos
while contador < 3:  # Condición
    print(contador)  # Mostramos el valor
    contador += 1  # Actualizamos
#
# Verás esto
# Verás 0, 1, 2 en líneas separadas.
#
# Por qué funciona
# El contador aumenta hasta que la condición falla.
#
# Lo típico que sale mal
# - Olvidar contador += 1.
# - Usar una condición que nunca cambia.
""",
            ),
            (
                "break en bucle",
                """# Aprende esto
# Aprenderás a salir de un bucle con break.
# Verás el corte antes de completar range.
# Entenderás la condición de salida.
#
# Haz esto
for numero in range(5):  # Recorremos 0-4
    if numero == 3:  # Condición de salida
        break  # Cortamos
    print(numero)  # Mostramos el número
#
# Verás esto
# Verás 0, 1, 2.
#
# Por qué funciona
# break detiene el bucle cuando numero == 3.
#
# Lo típico que sale mal
# - Indentar mal el break.
# - Usar break sin condición clara.
""",
            ),
            (
                "continue en bucle",
                """# Aprende esto
# Aprenderás a saltar una iteración con continue.
# Verás cómo omitir un valor específico.
# Entenderás su efecto en el flujo.
#
# Haz esto
for numero in range(5):  # Recorremos 0-4
    if numero == 2:  # Valor a omitir
        continue  # Saltamos
    print(numero)  # Mostramos el resto
#
# Verás esto
# Verás 0, 1, 3, 4.
#
# Por qué funciona
# continue salta solo la iteración actual.
#
# Lo típico que sale mal
# - Poner continue después del trabajo útil.
# - Olvidar que el resto del bloque se omite.
""",
            ),
            (
                "Sumar con acumulador",
                """# Aprende esto
# Aprenderás a acumular valores en un bucle.
# Verás cómo sumar una serie.
# Entenderás el patrón acumulador.
#
# Haz esto
total = 0  # Acumulador
for numero in range(1, 4):  # 1,2,3
    total += numero  # Sumamos
print(total)  # Mostramos el total
#
# Verás esto
# Verás 6.
#
# Por qué funciona
# total guarda la suma acumulada.
#
# Lo típico que sale mal
# - No inicializar total en 0.
# - Usar range incorrecto.
""",
            ),
            (
                "Buscar con while",
                """# Aprende esto
# Aprenderás a buscar un valor con while.
# Verás cómo detenerte cuando lo encuentras.
# Entenderás el uso de banderas.
#
# Haz esto
objetivo = 3  # Valor objetivo
actual = 0  # Valor inicial
while actual <= 5:  # Repetimos
    if actual == objetivo:  # Si encontramos
        print("Encontrado")  # Mensaje
        break  # Salimos
    actual += 1  # Actualizamos
#
# Verás esto
# Verás "Encontrado".
#
# Por qué funciona
# El bucle termina cuando se cumple la condición.
#
# Lo típico que sale mal
# - Olvidar el break y seguir iterando.
# - No actualizar actual y entrar en bucle infinito.
""",
            ),
            (
                "Iterar con índice",
                """# Aprende esto
# Aprenderás a usar índices con range(len()).
# Verás cómo acceder por posición.
# Entenderás cuándo es necesario.
#
# Haz esto
nombres = ["Ana", "Luis", "Marta"]  # Lista
for i in range(len(nombres)):  # Índices
    print(i, nombres[i])  # Índice y valor
#
# Verás esto
# Verás 0 Ana, 1 Luis, 2 Marta.
#
# Por qué funciona
# range(len()) recorre posiciones válidas.
#
# Lo típico que sale mal
# - Usar len y luego acceder fuera de rango.
# - Usar índices cuando no hace falta.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Imprime los números del 0 al 4 usando for y range.",
                "hints": ["Usa range(5).", "Recuerda el : en el for."],
                "solution": """for i in range(5):
    print(i)""",
            },
            {
                "question": "Recorre una lista de tres colores e imprime cada uno.",
                "hints": ["Usa for color in colores.", "Define la lista antes."],
                "solution": """colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)""",
            },
            {
                "question": "Usa while para contar de 1 a 3.",
                "hints": ["Inicializa un contador.", "Actualiza el contador dentro del bucle."],
                "solution": """contador = 1
while contador <= 3:
    print(contador)
    contador += 1""",
            },
            {
                "question": "Detén un bucle for cuando el número sea 2 usando break.",
                "hints": ["Compara con ==.", "Coloca break dentro del if."],
                "solution": """for numero in range(5):
    if numero == 2:
        break
    print(numero)""",
            },
            {
                "question": "Salta el número 3 en un for usando continue.",
                "hints": ["Usa if numero == 3.", "continue salta la iteración."],
                "solution": """for numero in range(5):
    if numero == 3:
        continue
    print(numero)""",
            },
            {
                "question": "Suma los números del 1 al 4 con un acumulador.",
                "hints": ["Inicializa total en 0.", "Suma en cada iteración."],
                "solution": """total = 0
for numero in range(1, 5):
    total += numero
print(total)""",
            },
        ]

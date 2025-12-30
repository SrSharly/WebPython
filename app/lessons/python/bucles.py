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

### Micro-ejemplo: range con inicio y paso
Cuando necesitas saltos o empezar en otro valor, usa `range(inicio, fin, paso)`.

**Así se escribe**
```py
for i in range(2, 10, 2):
    print(i)
```

**Error típico (❌)**
```py
for i in range(1, 5, 0):
    print(i)
```

**Qué significa el error**
`ValueError: range() arg 3 must not be zero` porque el paso no puede ser 0.

**Cómo se arregla**
Usa un paso distinto de cero, por ejemplo `range(1, 5, 1)` o `range(1, 5, -1)` si vas hacia atrás.

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



## Operaciones y métodos más útiles
### Strings (`str`)
1) `upper()` ⭐  
Qué hace: convierte a mayúsculas.  
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
Por qué funciona: `upper()` crea un texto nuevo con mayúsculas.  
Lo típico que sale mal: olvidar paréntesis; creer que cambia el string original.

2) `lower()` ⭐  
Qué hace: convierte a minúsculas.  
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
Lo típico que sale mal: no normalizar ambos lados; asumir mutación in-place.

3) `strip()` ⭐  
Qué hace: quita espacios al inicio y final.  
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
Por qué funciona: recorta whitespace en bordes.  
Lo típico que sale mal: esperar que quite espacios internos; no guardar el resultado.

4) `replace()` ⭐  
Qué hace: reemplaza un fragmento por otro.  
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
Por qué funciona: genera un string nuevo con reemplazo.  
Lo típico que sale mal: olvidar el segundo argumento; creer que modifica en sitio.

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
Verás esto: `['a', 'b', 'c']`.  
Por qué funciona: corta según el separador.  
Lo típico que sale mal: confundir split con slicing; usar separador incorrecto.

6) `join()`  
Qué hace: une textos con un separador.  
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
Por qué funciona: `join()` es método del separador.  
Lo típico que sale mal: pasar elementos no string; invertir el orden.

### Números (`int` / `float`)
1) `round()` ⭐  
Qué hace: redondea a n decimales.  
Así se escribe:
```py
precio = 3.1416
aprox = round(precio, 2)
```
Error típico:
```py
aprox = round("3.1416", 2)
```
Verás esto: `3.14`.  
Por qué funciona: `round` opera sobre números.  
Lo típico que sale mal: pasar strings; esperar más decimales sin indicar n.

2) `abs()` ⭐  
Qué hace: devuelve el valor absoluto.  
Así se escribe:
```py
delta = abs(-5)
```
Error típico:
```py
delta = abs[-5]
```
Verás esto: `5`.  
Por qué funciona: elimina el signo negativo.  
Lo típico que sale mal: olvidar paréntesis; pasar texto no numérico.

3) `int()` ⭐  
Qué hace: convierte a entero (trunca decimales).  
Así se escribe:
```py
cantidad = int("12")
```
Error típico:
```py
cantidad = int("12.5")
```
Verás esto: `12`.  
Por qué funciona: `int` convierte strings numéricos enteros.  
Lo típico que sale mal: usar strings con punto; asumir redondeo en vez de truncado.

4) `float()` ⭐  
Qué hace: convierte a flotante.  
Así se escribe:
```py
valor = float("3.5")
```
Error típico:
```py
valor = float("tres")
```
Verás esto: `3.5`.  
Por qué funciona: `float` interpreta strings numéricos.  
Lo típico que sale mal: usar textos no numéricos; confundir coma con punto.

5) `//` (división entera)  
Qué hace: divide y descarta decimales.  
Así se escribe:
```py
resultado = 7 // 2
```
Error típico:
```py
resultado = 7 // 0
```
Verás esto: `3`.  
Por qué funciona: aplica división entera.  
Lo típico que sale mal: división por cero; asumir que redondea (en realidad trunca).

6) `%` (módulo)  
Qué hace: devuelve el resto de una división.  
Así se escribe:
```py
resto = 7 % 2
```
Error típico:
```py
resto = 7 % 0
```
Verás esto: `1`.  
Por qué funciona: calcula el residuo.  
Lo típico que sale mal: división por cero; usarlo con floats y esperar enteros.

### Booleanos (`bool`)
1) `bool()` ⭐  
Qué hace: convierte un valor a True/False.  
Así se escribe:
```py
activo = bool(1)
```
Error típico:
```py
activo = bool("0")
```
Verás esto: `True`.  
Por qué funciona: cualquier string no vacío es True.  
Lo típico que sale mal: asumir que "0" es False; no validar entradas.

2) `not` ⭐  
Qué hace: niega una condición.  
Así se escribe:
```py
es_vacio = not True
```
Error típico:
```py
es_vacio = not
```
Verás esto: `False`.  
Por qué funciona: invierte el valor booleano.  
Lo típico que sale mal: usarlo sin operando; encadenar sin paréntesis.

3) `and` ⭐  
Qué hace: True solo si ambas condiciones son True.  
Así se escribe:
```py
permitido = True and False
```
Error típico:
```py
permitido = True and
```
Verás esto: `False`.  
Por qué funciona: evalúa ambas condiciones.  
Lo típico que sale mal: olvidar el segundo operando; confiar en el orden sin paréntesis.

4) `or` ⭐  
Qué hace: True si alguna condición es True.  
Así se escribe:
```py
permitido = False or True
```
Error típico:
```py
permitido = False or
```
Verás esto: `True`.  
Por qué funciona: basta un True para pasar.  
Lo típico que sale mal: olvidar el segundo operando; asumir que evalúa siempre ambas partes.

5) `==` (comparación)  
Qué hace: compara igualdad.  
Así se escribe:
```py
es_cero = (0 == 0)
```
Error típico:
```py
es_cero = (0 = 0)
```
Verás esto: `True`.  
Por qué funciona: `==` compara valores.  
Lo típico que sale mal: usar `=` por accidente; comparar tipos incompatibles.

6) `is` (identidad)  
Qué hace: comprueba identidad, útil con `None`.  
Así se escribe:
```py
valor = None
es_nulo = valor is None
```
Error típico:
```py
es_nulo = valor == None
```
Verás esto: `True`.  
Por qué funciona: `is` compara identidad exacta.  
Lo típico que sale mal: usar `==` en lugar de `is`; comparar objetos mutables.

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

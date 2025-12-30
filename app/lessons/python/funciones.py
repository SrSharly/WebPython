from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class FuncionesLesson(Lesson):
    TITLE = "Funciones"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["funciones", "def", "return", "parametros"]

    def summary(self) -> str:
        return (
            "Aprende a crear funciones claras con parámetros y return, y evita errores comunes como "
            "olvidar devolver valores o confundir print con return."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: funciones para reutilizar y ordenar
Una función es un bloque de código con nombre que puedes reutilizar. Te permite dividir problemas en pasos pequeños y
predecibles. La sintaxis tiene tres piezas: `def`, parámetros y `return`.

En esta lección aprenderás a crear funciones desde cero con micro-snippets correctos e incorrectos para cada concepto.

## Paso 1: definir una función con def
`def` crea una función y los paréntesis contienen los parámetros.

**Así se escribe**
```py
def saludar(nombre):
    print(f"Hola {nombre}")
```

**Error típico (❌)**
```py
def saludar nombre:
    print("Hola")
```

**Qué significa el error**
`SyntaxError` porque faltan paréntesis alrededor de los parámetros.

**Cómo se arregla**
Agrega paréntesis: `def saludar(nombre):`.

## Paso 2: parámetros y argumentos
Los parámetros son nombres dentro de la función; los argumentos son los valores que pasas al llamarla.

**Así se escribe**
```py
def sumar(a, b):
    return a + b

resultado = sumar(2, 3)
```

**Error típico (❌)**
```py
def sumar(a, b):
    return a + b

resultado = sumar(2)
```

**Qué significa el error**
`TypeError` indica que falta un argumento requerido.

**Cómo se arregla**
Pasa todos los argumentos necesarios o define valores por defecto.

### Así se escribe: pasar datos con input
```py
def presentar(nombre):
    return f"Hola {nombre}"

usuario = input("Nombre: ")
print(presentar(usuario))
```

### Error típico: olvidar convertir input
```py
def duplicar(numero):
    return numero * 2

valor = input("Número: ")
print(duplicar(valor) + 1)
```

```py
TypeError: can only concatenate str (not "int") to str
```

Explicación breve: `input()` devuelve `str`; conviértelo a `int` antes de operar.

## Paso 3: return y valores de salida
`return` envía un resultado al exterior. Si no lo usas, la función devuelve `None`.

**Así se escribe**
```py
def area_cuadrado(lado):
    return lado * lado
```

**Error típico (❌)**
```py
def area_cuadrado(lado):
    lado * lado
```

**Qué significa el error**
No hay error de sintaxis, pero la función devuelve `None` porque no hay `return`.

**Cómo se arregla**
Agrega `return` para devolver el resultado.

## Paso 4: no confundir print con return
`print` muestra en pantalla, `return` entrega un valor para seguir trabajando.

**Así se escribe**
```py
def duplicar(n):
    return n * 2

resultado = duplicar(4)
```

**Error típico (❌)**
```py
def duplicar(n):
    print(n * 2)

resultado = duplicar(4)
```

**Qué significa el error**
La función imprime el resultado pero devuelve `None`. `resultado` queda vacío.

**Cómo se arregla**
Usa `return` cuando necesitas guardar o reutilizar el valor.

## Paso 5: resumen para funciones claras
Define la función con `def`, recibe parámetros, calcula y devuelve con `return`. Usa `print` solo para mostrar, no para
pasar datos a otras partes del programa.



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
                "Olvidar los paréntesis en def",
                "`def saludar nombre:` provoca `SyntaxError`. Los parámetros van entre paréntesis.",
            ),
            (
                "Olvidar el return",
                "Si no hay `return`, la función devuelve `None` aunque calcule algo.",
            ),
            (
                "Confundir print con return",
                "Imprimir no devuelve. Usa `return` cuando necesitas el valor.",
            ),
            (
                "No pasar argumentos necesarios",
                "`TypeError` ocurre si faltan argumentos requeridos.",
            ),
            (
                "Pasar más argumentos de los necesarios",
                "También genera `TypeError`. Revisa la firma de la función.",
            ),
            (
                "Usar nombres poco claros",
                "Parámetros como `x` o `y` dificultan la lectura. Usa nombres descriptivos.",
            ),
            (
                "Modificar variables globales sin control",
                "Evita efectos secundarios: usa parámetros y valores devueltos.",
            ),
            (
                "No documentar qué devuelve",
                "Si no queda claro el tipo de retorno, el uso se vuelve confuso.",
            ),
            (
                "Repetir código en lugar de función",
                "Si repites bloques iguales, conviene crear una función.",
            ),
            (
                "No usar valores por defecto",
                "Si un argumento es opcional, define un valor por defecto para evitar errores.",
            ),
            (
                "Devolver múltiples cosas sin estructura",
                "Si devuelves varias cosas, considera usar tuplas y documentar el orden.",
            ),
            (
                "Llamar a la función antes de definirla",
                "En Python debes definir la función antes de usarla en el flujo.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Función básica",
                """# Aprende esto
# Aprenderás a definir una función simple.
# Verás cómo recibir un parámetro.
# Entenderás dónde se imprime el resultado.
#
# Haz esto
def saludar(nombre):  # Definimos la función
    print(f"Hola {nombre}")  # Mensaje

saludar("Ana")  # Llamamos la función
#
# Verás esto
# Verás "Hola Ana".
#
# Por qué funciona
# La función recibe el nombre y lo usa en el print.
#
# Lo típico que sale mal
# - Olvidar los paréntesis en def.
# - Llamar la función sin argumentos.
""",
            ),
            (
                "Función con return",
                """# Aprende esto
# Aprenderás a devolver un valor.
# Verás cómo usar el resultado.
# Entenderás la diferencia con print.
#
# Haz esto
def sumar(a, b):  # Definimos la función
    return a + b  # Devolvemos la suma

resultado = sumar(2, 3)  # Guardamos el resultado
print(resultado)  # Mostramos
#
# Verás esto
# Verás 5.
#
# Por qué funciona
# return envía el valor a quien llama.
#
# Lo típico que sale mal
# - Usar print en lugar de return.
# - No guardar el resultado.
""",
            ),
            (
                "Parámetros por defecto",
                """# Aprende esto
# Aprenderás a definir valores por defecto.
# Verás cómo omitir argumentos.
# Entenderás la flexibilidad.
#
# Haz esto
def saludar(nombre, prefijo="Hola"):  # Valor por defecto
    return f"{prefijo} {nombre}"  # Construimos mensaje

print(saludar("Ana"))  # Usamos valor por defecto
print(saludar("Luis", "Buenos días"))  # Usamos prefijo
#
# Verás esto
# Verás "Hola Ana" y "Buenos días Luis".
#
# Por qué funciona
# Si no pasas prefijo, se usa el valor por defecto.
#
# Lo típico que sale mal
# - Poner el parámetro con defecto antes de uno obligatorio.
# - Olvidar que el valor por defecto se evalúa una vez.
""",
            ),
            (
                "Devolver None sin querer",
                """# Aprende esto
# Aprenderás qué pasa si no devuelves valor.
# Verás el resultado None.
# Entenderás por qué hay que usar return.
#
# Haz esto
def cuadrado(n):  # Función
    n * n  # Calculamos pero no devolvemos

resultado = cuadrado(4)  # Guardamos
print(resultado)  # Mostramos
#
# Verás esto
# Verás None.
#
# Por qué funciona
# Sin return, Python devuelve None.
#
# Lo típico que sale mal
# - Creer que una expresión se devuelve sola.
# - No revisar el valor de resultado.
""",
            ),
            (
                "Return vs print",
                """# Aprende esto
# Aprenderás la diferencia entre imprimir y devolver.
# Verás cómo usar el valor fuera de la función.
# Entenderás la reutilización.
#
# Haz esto
def duplicar(n):  # Función
    return n * 2  # Devolvemos

valor = duplicar(5)  # Guardamos
print(valor)  # Mostramos
#
# Verás esto
# Verás 10.
#
# Por qué funciona
# El valor devuelto se guarda en valor.
#
# Lo típico que sale mal
# - Usar print en la función y esperar un return.
# - No capturar el resultado.
""",
            ),
            (
                "Función con validación",
                """# Aprende esto
# Aprenderás a validar dentro de una función.
# Verás un return temprano.
# Entenderás cómo manejar errores simples.
#
# Haz esto
def dividir(a, b):  # Función
    if b == 0:  # Validación
        return None  # Evitamos error
    return a / b  # Devolvemos resultado

print(dividir(10, 2))  # Caso válido
print(dividir(10, 0))  # Caso inválido
#
# Verás esto
# Verás 5.0 y None.
#
# Por qué funciona
# Se evita la división por cero con un return temprano.
#
# Lo típico que sale mal
# - Olvidar la validación y lanzar ZeroDivisionError.
# - Devolver valores inconsistentes sin documentar.
""",
            ),
            (
                "Reutilizar funciones",
                """# Aprende esto
# Aprenderás a reutilizar funciones en varios lugares.
# Verás cómo evitar duplicación.
# Entenderás el beneficio del diseño modular.
#
# Haz esto
def precio_con_iva(precio, iva):  # Función
    return precio * (1 + iva)  # Calculamos

producto_a = precio_con_iva(10, 0.21)  # Primer uso
producto_b = precio_con_iva(20, 0.21)  # Segundo uso
print(producto_a)  # Mostramos
print(producto_b)  # Mostramos
#
# Verás esto
# Verás 12.1 y 24.2.
#
# Por qué funciona
# La lógica está en una función reutilizable.
#
# Lo típico que sale mal
# - Repetir el cálculo en lugar de usar la función.
# - Mezclar unidades sin documentarlas.
""",
            ),
            (
                "Funciones pequeñas",
                """# Aprende esto
# Aprenderás a dividir tareas en funciones pequeñas.
# Verás una función que calcula y otra que muestra.
# Entenderás la claridad que aporta.
#
# Haz esto
def calcular_total(precio, cantidad):  # Función de cálculo
    return precio * cantidad  # Total


def mostrar_total(total):  # Función de presentación
    print(f"Total: {total}")  # Mensaje


valor = calcular_total(5, 3)  # Calculamos
mostrar_total(valor)  # Mostramos
#
# Verás esto
# Verás "Total: 15".
#
# Por qué funciona
# Separar cálculo y presentación mejora la claridad.
#
# Lo típico que sale mal
# - Poner todo en una sola función gigante.
# - Mezclar print y return sin necesidad.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una función `saludar` que reciba un nombre y muestre un saludo.",
                "hints": ["Usa def saludar(nombre).", "Usa print dentro."],
                "solution": """def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Ana")""",
            },
            {
                "question": "Crea una función `sumar` que reciba dos números y devuelva la suma.",
                "hints": ["Usa return.", "Guarda el resultado al llamar."],
                "solution": """def sumar(a, b):
    return a + b

resultado = sumar(2, 3)
print(resultado)""",
            },
            {
                "question": "Define una función `cuadrado` y muestra el resultado de elevar 5 al cuadrado.",
                "hints": ["Usa return.", "Llama la función con 5."],
                "solution": """def cuadrado(n):
    return n * n

print(cuadrado(5))""",
            },
            {
                "question": "Crea una función con un parámetro por defecto para el prefijo del saludo.",
                "hints": ["Agrega prefijo=\"Hola\".", "Devuelve el texto."],
                "solution": """def saludar(nombre, prefijo="Hola"):
    return f"{prefijo} {nombre}"

print(saludar("Ana"))""",
            },
            {
                "question": "Escribe una función `duplicar` que devuelva el doble y guarda el resultado.",
                "hints": ["No uses print en la función.", "Usa return."],
                "solution": """def duplicar(n):
    return n * 2

resultado = duplicar(4)
print(resultado)""",
            },
            {
                "question": "Crea una función `dividir` que devuelva None si el divisor es 0.",
                "hints": ["Usa if b == 0.", "Retorna None en ese caso."],
                "solution": """def dividir(a, b):
    if b == 0:
        return None
    return a / b

print(dividir(10, 0))""",
            },
        ]

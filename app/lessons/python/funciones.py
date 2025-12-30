from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class FuncionesLesson(Lesson):
    TITLE = "Funciones"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["funciones", "parametros", "retorno", "scope"]

    def summary(self) -> str:
        return (
            "Aprende desde cero qué es una función, cuándo usarla, cómo recibir argumentos y "
            "devolver resultados con buenas prácticas claras."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: por qué las funciones cambian tu forma de programar
Una función es un bloque de código con nombre que encapsula una tarea. Te permite **reutilizar lógica**, reducir errores
por copia y separar problemas grandes en partes pequeñas. Cuando entiendes funciones, tu código se vuelve más claro,
más fácil de probar y más fácil de mantener.

## Paso 1: Definir una función con un objetivo claro
Definir una función es darle un nombre y un conjunto de pasos.

**Aprende esto**
- Aprenderás a crear funciones que resuelven una tarea concreta.
- Verás cómo `return` devuelve un resultado al llamador.

**Haz esto**
```
def saludar(nombre):  # Definimos la función con un parámetro
    mensaje = "Hola " + nombre  # Construimos el texto de saludo
    return mensaje  # Devolvemos el texto al llamar a la función

saludo = saludar("Ana")  # Llamamos a la función con un argumento
print(saludo)  # Mostramos el resultado
```

**Verás esto**
Verás `Hola Ana` como salida.

**Por qué funciona**
`return` entrega el valor al punto donde se llamó la función. La variable `saludo` recibe ese valor.

**Lo típico que sale mal**
- Olvidar `return` y obtener `None` cuando esperabas un texto.
- Nombrar la función con algo genérico y perder claridad.

## Paso 2: Parámetros y argumentos
Un **parámetro** es el nombre dentro de la función; un **argumento** es el valor real que pasas.

**Aprende esto**
- Aprenderás a definir parámetros para que la función sea flexible.
- Verás cómo pasar argumentos de forma ordenada.

**Haz esto**
```
def sumar(a, b):  # Parámetros a y b
    resultado = a + b  # Sumamos los valores recibidos
    return resultado  # Devolvemos el resultado

suma = sumar(3, 5)  # 3 y 5 son argumentos
print(suma)  # Mostramos la suma
```

**Verás esto**
Verás `8` como salida.

**Por qué funciona**
Los valores 3 y 5 se asignan a `a` y `b`, y la función devuelve la suma.

**Lo típico que sale mal**
- Cambiar el orden de los argumentos y obtener un resultado incorrecto.
- Usar parámetros con nombres confusos.

## Paso 3: Valores por defecto
Puedes definir un valor por defecto para parámetros que no siempre cambian.

**Aprende esto**
- Aprenderás a definir defaults para simplificar llamadas.
- Verás cómo sobrescribirlos cuando sea necesario.

**Haz esto**
```
def potencia(base, exponente=2):  # Default en exponente
    resultado = base ** exponente  # Calculamos la potencia
    return resultado  # Devolvemos el resultado

cuadrado = potencia(4)  # Usa exponente 2
cubo = potencia(4, 3)  # Cambiamos el exponente
print(cuadrado)  # Mostramos 16
print(cubo)  # Mostramos 64
```

**Verás esto**
Verás `16` y `64` en líneas separadas.

**Por qué funciona**
Si no envías `exponente`, Python usa el valor por defecto. Si lo envías, reemplaza ese valor.

**Lo típico que sale mal**
- Usar listas o diccionarios como default y compartirlos sin querer.
- Olvidar que los defaults se evalúan una sola vez.

## Paso 4: Scope y variables locales
Las variables dentro de una función no afectan automáticamente a las de afuera.

**Aprende esto**
- Aprenderás a distinguir variables locales y globales.
- Verás cómo una función puede usar datos sin modificar el exterior.

**Haz esto**
```
contador = 0  # Variable global

def sumar_uno(valor):  # Recibimos un número
    nuevo_valor = valor + 1  # Calculamos un nuevo valor
    return nuevo_valor  # Devolvemos el nuevo valor

contador = sumar_uno(contador)  # Actualizamos con el retorno
print(contador)  # Mostramos el contador actualizado
```

**Verás esto**
Verás `1` como salida.

**Por qué funciona**
La función trabaja con una copia del valor y devuelve el resultado. Tú decides cuándo actualizar la variable externa.

**Lo típico que sale mal**
- Esperar que la función cambie una variable global automáticamente.
- Usar `global` sin necesidad y perder claridad.

## Paso 5: *args y **kwargs
Estas herramientas sirven para recibir muchos argumentos sin definirlos uno por uno.

**Aprende esto**
- Aprenderás a agrupar argumentos posicionales con `*args`.
- Verás cómo `**kwargs` captura argumentos con nombre.

**Haz esto**
```
def resumen(*args, **kwargs):  # Recibimos muchos datos
    total = sum(args)  # Sumamos los valores posicionales
    etiqueta = kwargs.get("etiqueta", "Total")  # Leemos un nombre opcional
    mensaje = etiqueta + ": " + str(total)  # Construimos el mensaje
    return mensaje  # Devolvemos el texto final

print(resumen(1, 2, 3, etiqueta="Suma"))  # Llamamos con etiqueta
```

**Verás esto**
Verás `Suma: 6`.

**Por qué funciona**
`*args` llega como tupla y `**kwargs` como diccionario; ambos se pueden leer dentro de la función.

**Lo típico que sale mal**
- Olvidar que `args` es una tupla y no admite `append`.
- Usar `kwargs['clave']` sin verificar si la clave existe.

## Paso 6: Docstrings y claridad
Una docstring explica la intención de la función para quien lee el código.

**Aprende esto**
- Aprenderás a describir tu función dentro de ella misma.
- Verás cómo mejorar la comprensión sin leer el cuerpo completo.

**Haz esto**
```
def promedio(valores):  # Función de ejemplo
    """Calcula el promedio de una lista de números."""  # Docstring corta
    total = sum(valores)  # Sumamos los valores
    cantidad = len(valores)  # Contamos cuántos hay
    return total / cantidad  # Devolvemos el promedio

print(promedio([10, 20, 30]))  # Llamamos a la función
```

**Verás esto**
Verás `20.0` como salida.

**Por qué funciona**
`sum` y `len` calculan el total y la cantidad; el resultado es su división.

**Lo típico que sale mal**
- No explicar qué recibe y qué devuelve la función.
- Usar docstrings vagas como “hace cosas”.

## Más allá (nivel pro)
Las funciones también se benefician de pequeñas mejoras que facilitan el trabajo en equipo.

**Aprende esto**
- Aprenderás a usar type hints para comunicar expectativas.
- Verás cómo devolver múltiples valores con una tupla.

**Haz esto**
```
def dividir(a: float, b: float) -> tuple[float, float]:  # Indicamos tipos
    cociente = a // b  # División entera
    resto = a % b  # Resto de la división
    return cociente, resto  # Devolvemos dos valores

q, r = dividir(10, 3)  # Desempaquetamos la tupla
print(q, r)  # Mostramos cociente y resto
```

**Verás esto**
Verás `3 1`.

**Por qué funciona**
La función devuelve una tupla y Python permite desempaquetarla en dos variables.

**Lo típico que sale mal**
- Olvidar el orden de la tupla y confundir cociente con resto.
- Asumir que los type hints validan en tiempo de ejecución (no lo hacen).
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Olvidar return",
                "Si una función no usa return, devuelve None aunque haya calculado algo.",
            ),
            (
                "Repetir código en lugar de crear una función",
                "Duplicar lógica dificulta el mantenimiento y aumenta errores.",
            ),
            (
                "Confundir parámetros con argumentos",
                "El parámetro es el nombre en la definición; el argumento es el valor real.",
            ),
            (
                "Usar mutables como default",
                "Listas o diccionarios como default se comparten entre llamadas.",
            ),
            (
                "No documentar la función",
                "Sin docstring, otros no saben qué espera ni qué devuelve.",
            ),
            (
                "Cambiar variables globales sin control",
                "Modificar globals desde funciones vuelve el flujo impredecible.",
            ),
            (
                "Ignorar el orden de argumentos",
                "Pasar argumentos en orden incorrecto cambia el resultado.",
            ),
            (
                "No validar entradas",
                "Asumir que llegan valores correctos causa errores en producción.",
            ),
            (
                "Olvidar desempacar la tupla",
                "Si una función devuelve varios valores, hay que capturarlos correctamente.",
            ),
            (
                "Usar nombres ambiguos",
                "Funciones llamadas do o run no dicen qué hacen realmente.",
            ),
            (
                "Retornar múltiples tipos",
                "Devolver a veces un número y a veces texto complica el uso posterior.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Definir y llamar una función",
                """# Aprende esto
# Aprenderás a definir una función con return.
# Verás cómo reutilizar el resultado al llamar.
#
# Haz esto
def saludar(nombre):  # Definimos una función con parámetro
    mensaje = "Hola " + nombre  # Construimos el saludo
    return mensaje  # Devolvemos el texto

saludo = saludar("Ana")  # Llamamos con un argumento
print(saludo)  # Mostramos el resultado
#
# Verás esto
# Verás "Hola Ana" como salida.
#
# Por qué funciona
# return envía el valor de vuelta a la línea que llamó la función.
#
# Lo típico que sale mal
# - Olvidar return y recibir None.
# - Usar un nombre de función poco claro.
""",
            ),
            (
                "Parámetros y argumentos",
                """# Aprende esto
# Aprenderás a usar parámetros para sumar valores.
# Verás cómo los argumentos se asignan a esos parámetros.
#
# Haz esto
def sumar(a, b):  # Parámetros a y b
    resultado = a + b  # Sumamos
    return resultado  # Devolvemos la suma

suma = sumar(3, 5)  # Argumentos 3 y 5
print(suma)  # Mostramos el resultado
#
# Verás esto
# Verás 8 como salida.
#
# Por qué funciona
# a y b reciben los valores enviados y la función devuelve a + b.
#
# Lo típico que sale mal
# - Cambiar el orden de argumentos.
# - Usar nombres de parámetros confusos.
""",
            ),
            (
                "Valores por defecto",
                """# Aprende esto
# Aprenderás a definir un parámetro con valor por defecto.
# Verás cómo sobrescribirlo cuando lo necesites.
#
# Haz esto
def potencia(base, exponente=2):  # Default en exponente
    resultado = base ** exponente  # Calculamos potencia
    return resultado  # Devolvemos el resultado

print(potencia(4))  # Usa exponente 2
print(potencia(4, 3))  # Cambia el exponente
#
# Verás esto
# Verás 16 y 64 como salida.
#
# Por qué funciona
# Si no envías el argumento, se usa el valor por defecto.
#
# Lo típico que sale mal
# - Usar listas como default.
# - Olvidar que el default se evalúa una vez.
""",
            ),
            (
                "Scope y variables locales",
                """# Aprende esto
# Aprenderás a trabajar con variables locales.
# Verás cómo actualizar una global con el retorno.
#
# Haz esto
contador = 0  # Variable global

def sumar_uno(valor):  # Recibimos un valor
    nuevo_valor = valor + 1  # Incrementamos
    return nuevo_valor  # Devolvemos el nuevo valor

contador = sumar_uno(contador)  # Actualizamos desde fuera
print(contador)  # Mostramos el contador
#
# Verás esto
# Verás 1 como salida.
#
# Por qué funciona
# La función devuelve el nuevo valor y tú decides asignarlo.
#
# Lo típico que sale mal
# - Esperar cambios en globals sin reasignar.
# - Usar global sin necesidad.
""",
            ),
            (
                "*args y **kwargs",
                """# Aprende esto
# Aprenderás a recibir muchos argumentos.
# Verás cómo combinar args con un nombre opcional.
#
# Haz esto
def resumen(*args, **kwargs):  # Recibimos valores
    total = sum(args)  # Sumamos los posicionales
    etiqueta = kwargs.get("etiqueta", "Total")  # Leemos la etiqueta
    mensaje = etiqueta + ": " + str(total)  # Construimos el mensaje
    return mensaje  # Devolvemos el mensaje

print(resumen(1, 2, 3, etiqueta="Suma"))  # Llamamos
#
# Verás esto
# Verás "Suma: 6".
#
# Por qué funciona
# args llega como tupla y kwargs como diccionario.
#
# Lo típico que sale mal
# - Usar args como si fuera lista.
# - Acceder a kwargs sin verificar la clave.
""",
            ),
            (
                "Docstring clara",
                """# Aprende esto
# Aprenderás a documentar tu función.
# Verás cómo la docstring explica su objetivo.
#
# Haz esto
def promedio(valores):  # Función de ejemplo
    """Calcula el promedio de una lista de números."""  # Docstring
    total = sum(valores)  # Sumamos
    cantidad = len(valores)  # Contamos
    return total / cantidad  # Dividimos

print(promedio([10, 20, 30]))  # Llamamos
#
# Verás esto
# Verás 20.0 como salida.
#
# Por qué funciona
# sum y len dan total y cantidad para el promedio.
#
# Lo típico que sale mal
# - No explicar qué recibe la función.
# - Dejar docstrings vagas.
""",
            ),
            (
                "Type hints simples",
                """# Aprende esto
# Aprenderás a indicar tipos de entrada y salida.
# Verás que ayudan a leer la intención.
#
# Haz esto
def area_cuadrado(lado: float) -> float:  # Indicamos tipo
    area = lado * lado  # Calculamos el área
    return area  # Devolvemos el resultado

resultado = area_cuadrado(3.0)  # Llamamos a la función
print(resultado)  # Mostramos el área
#
# Verás esto
# Verás 9.0 como salida.
#
# Por qué funciona
# Los hints describen el tipo y la operación es un producto simple.
#
# Lo típico que sale mal
# - Creer que los hints validan en runtime.
# - Usar hints inconsistentes.
""",
            ),
            (
                "Devolver múltiples valores",
                """# Aprende esto
# Aprenderás a devolver dos valores en una tupla.
# Verás cómo desempaquetarlos correctamente.
#
# Haz esto
def dividir(a, b):  # Recibimos dos números
    cociente = a // b  # División entera
    resto = a % b  # Calculamos el resto
    return cociente, resto  # Devolvemos ambos

q, r = dividir(10, 3)  # Desempaquetamos la tupla
print(q, r)  # Mostramos los valores
#
# Verás esto
# Verás 3 1 como salida.
#
# Por qué funciona
# La función devuelve una tupla y Python permite desempaquetarla.
#
# Lo típico que sale mal
# - Olvidar el orden de los valores.
# - Guardar la tupla en una sola variable.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una función llamada duplicar que reciba un número y devuelva el doble.",
                "hints": ["Usa def y return"],
                "solution": "def duplicar(n):\n    return n * 2\n\nprint(duplicar(4))",
            },
            {
                "question": "Define una función con un parámetro por defecto llamado saludo que diga 'Hola'.",
                "hints": ["Usa saludo='Hola'"],
                "solution": "def saludar(nombre, saludo='Hola'):\n    return saludo + ' ' + nombre\n\nprint(saludar('Ana'))",
            },
            {
                "question": "Escribe una función que reciba una lista y devuelva su suma.",
                "hints": ["Usa sum()"],
                "solution": "def sumar_lista(valores):\n    return sum(valores)\n\nprint(sumar_lista([1, 2, 3]))",
            },
            {
                "question": "Crea una función que retorne cociente y resto de una división.",
                "hints": ["Usa // y %"],
                "solution": "def dividir(a, b):\n    return a // b, a % b\n\nq, r = dividir(10, 3)\nprint(q, r)",
            },
            {
                "question": "Usa *args para sumar cualquier cantidad de números.",
                "hints": ["Define def sumar(*args)"],
                "solution": "def sumar(*args):\n    return sum(args)\n\nprint(sumar(1, 2, 3, 4))",
            },
            {
                "question": "Crea una función con docstring que explique su propósito.",
                "hints": ["Incluye triple comillas"],
                "solution": "def area(lado):\n    \"\"\"Calcula el área de un cuadrado.\"\"\"\n    return lado * lado\n\nprint(area(5))",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget

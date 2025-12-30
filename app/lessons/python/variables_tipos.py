from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class VariablesTiposLesson(Lesson):
    TITLE = "Variables y tipos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["variables", "tipos", "mutabilidad", "tipado-dinámico"]

    def summary(self) -> str:
        return (
            "Aprende desde cero qué es una variable, cómo funcionan los tipos, y por qué "
            "la mutabilidad, las copias y las conversiones importan en tu día a día."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: ¿por qué importan las variables y los tipos?
Una variable es el nombre que usamos para **recordar un valor**. Los tipos nos dicen qué clase de dato es ese valor
(número, texto, lista, etc.). Entender ambos conceptos evita errores comunes: sumar texto con números, modificar
listas sin querer o comparar valores de forma incorrecta.

En este tutorial verás cómo asignar valores, cómo reconocer tipos, cómo cambia el comportamiento cuando un objeto
es mutable o inmutable y cómo hacer conversiones seguras. Cada paso trae un ejemplo completo con el mismo patrón
para que lo puedas repetir en tu práctica diaria.

## Paso 1: Asignar valores con intención
Cuando asignas un valor, no “guardas una caja”; **nombras un dato** para poder reutilizarlo.

**Aprende esto**
- Aprenderás a crear variables con nombres claros y a reutilizarlas.
- Verás que el nombre es una etiqueta, no el valor en sí.

**Haz esto**
```
nombre = "Ana"  # Guardamos un texto con el nombre
apellido = "López"  # Guardamos otro texto relacionado
nombre_completo = nombre + " " + apellido  # Concatenamos con un espacio
etiqueta = "Cliente"  # Guardamos un rol simple
mensaje = etiqueta + ": " + nombre_completo  # Construimos un mensaje legible
print(mensaje)  # Mostramos el resultado final
```

**Verás esto**
Verás un texto como: `Cliente: Ana López`.

**Por qué funciona**
Funciona porque `+` concatena strings, y cada variable apunta a un texto. El valor final se construye paso a paso.

**Lo típico que sale mal**
- Reutilizar nombres genéricos como `x` o `tmp` y perder el significado.
- Intentar concatenar texto con números sin convertirlos primero.

## Paso 2: Reconocer tipos básicos
Los tipos te dicen cómo se comporta el dato: sumar enteros no es lo mismo que juntar textos.

**Aprende esto**
- Aprenderás a distinguir `int`, `float`, `str` y `bool`.
- Verás cómo el tipo afecta las operaciones disponibles.

**Haz esto**
```
edad = 20  # int: número entero
altura = 1.72  # float: número decimal
activo = True  # bool: verdadero o falso
resumen = "Edad: " + str(edad)  # Convertimos int a str para unir textos
print(resumen)  # Mostramos el resumen
print(altura + 0.03)  # Sumamos un decimal a otro decimal
```

**Verás esto**
Verás un resumen con la edad y un número decimal ajustado (por ejemplo 1.75).

**Por qué funciona**
`str(edad)` convierte el entero en texto, lo que permite concatenar. Los floats permiten operaciones con decimales.

**Lo típico que sale mal**
- Olvidar `str()` al concatenar y obtener un error de tipos.
- Usar coma en lugar de punto para decimales (Python requiere punto).

## Paso 3: Tipado dinámico con cuidado
En Python puedes reasignar una variable con otro tipo, pero eso puede confundir si no lo haces con intención.

**Aprende esto**
- Aprenderás qué significa “tipado dinámico”.
- Verás por qué es mejor mantener un tipo por variable siempre que puedas.

**Haz esto**
```
valor = 10  # Iniciamos con un entero
valor = valor + 5  # Actualizamos con otro entero
valor = str(valor)  # Convertimos a texto para mostrarlo
etiqueta = "Total"  # Creamos un texto descriptivo
mensaje = etiqueta + ": " + valor  # Construimos el mensaje final
print(mensaje)  # Mostramos el texto completo
```

**Verás esto**
Verás algo como `Total: 15`.

**Por qué funciona**
Primero operamos con enteros, luego convertimos el resultado a texto para mostrarlo. El cambio de tipo está controlado.

**Lo típico que sale mal**
- Cambiar el tipo sin conversión explícita y romper operaciones posteriores.
- Reutilizar una variable para datos distintos y perder claridad.

## Paso 4: Mutabilidad: listas vs strings
Las listas son **mutables**: cambian en el mismo objeto. Los strings son **inmutables**: producen un nuevo valor.

**Aprende esto**
- Aprenderás a reconocer cuándo un objeto se modifica “en el mismo lugar”.
- Verás por qué un string necesita una nueva variable para cambiar.

**Haz esto**
```
compras = ["pan", "leche"]  # Lista inicial
compras.append("café")  # append agrega un elemento a la lista existente
texto = "hola"  # String original
texto_mayus = texto.upper()  # upper devuelve un nuevo string en mayúsculas
print(compras)  # Mostramos la lista modificada
print(texto, texto_mayus)  # Mostramos el original y el nuevo string
```

**Verás esto**
Verás la lista con tres elementos y el texto original junto a su versión en mayúsculas.

**Por qué funciona**
`append` modifica la lista en sitio. `upper()` no cambia el string original porque los strings son inmutables.

**Lo típico que sale mal**
- Esperar que `upper()` cambie el string sin reasignarlo.
- Pensar que `append` crea una lista nueva (modifica la existente).

## Paso 5: Alias y copias
Asignar una lista a otra variable crea un **alias**, no una copia. Para independencia real, hay que copiar.

**Aprende esto**
- Aprenderás la diferencia entre alias y copia.
- Verás cómo evitar modificar datos sin querer.

**Haz esto**
```
original = [1, 2]  # Lista original
alias = original  # Alias: apunta al mismo objeto
alias.append(3)  # Modifica la misma lista
copia = original.copy()  # Copia superficial independiente
copia.append(99)  # Solo cambia la copia
print(original)  # Mostramos la lista original
```

**Verás esto**
Verás que `original` tiene `[1, 2, 3]` y no incluye el 99.

**Por qué funciona**
`alias` y `original` apuntan al mismo objeto, pero `copy()` crea una nueva lista con los mismos valores.

**Lo típico que sale mal**
- Modificar un alias pensando que es una copia.
- Usar `list_a = list_b` cuando se esperaba independencia.

## Paso 6: Conversiones explícitas y None
Convertir tipos es esencial cuando recibes texto de un usuario o de un archivo. `None` indica ausencia de valor.

**Aprende esto**
- Aprenderás a convertir texto a número de forma controlada.
- Verás cómo comprobar si un valor aún no existe usando `None`.

**Haz esto**
```
texto = "42"  # Texto numérico
numero = int(texto)  # Convertimos a entero
resultado = None  # Aún no hay resultado
resultado = numero + 8  # Ahora sí hay resultado numérico
if resultado is not None:  # Comprobamos que existe
    print(resultado)  # Mostramos el resultado
```

**Verás esto**
Verás el número `50` en pantalla.

**Por qué funciona**
`int()` convierte texto numérico a entero y `is not None` confirma que el valor ya fue calculado.

**Lo típico que sale mal**
- Usar `== None` en lugar de `is None`.
- Asumir que `None` equivale a 0.

## Más allá (nivel pro)
Cuando ya dominas lo básico, conviene entender matices que aparecen en proyectos reales.

**Aprende esto**
- Aprenderás la diferencia entre copia superficial y profunda con listas anidadas.
- Verás por qué `is` sirve para identidad y no para comparar valores numéricos.

**Haz esto**
```
matriz = [[1], [2]]  # Lista con listas internas
copia_superficial = matriz.copy()  # Copia la lista externa
copia_superficial[0].append(9)  # Modifica también la lista interna original
valor = None  # Valor especial de ausencia
es_mismo_objeto = valor is None  # Comprobamos identidad con None
print(matriz)  # Mostramos la matriz original afectada
print(es_mismo_objeto)  # Mostramos True porque es el mismo objeto None
```

**Verás esto**
Verás que la primera sublista quedó con `[1, 9]` y que la comparación con `None` devuelve `True`.

**Por qué funciona**
La copia superficial no duplica las listas internas. `is` verifica si dos referencias apuntan al mismo objeto.

**Lo típico que sale mal**
- Usar `is` para comparar enteros o strings y obtener resultados inconsistentes.
- Creer que `copy()` también copia las listas internas.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir alias con copia",
                "Asignar b = a en listas no copia, solo crea un alias. Usa a.copy() si quieres independencia.",
            ),
            (
                "Mezclar tipos en operaciones",
                "\"3\" + 4 falla porque str e int no se combinan sin convertir.",
            ),
            (
                "Cambiar de tipo sin avisar",
                "Reusar la misma variable con tipos distintos vuelve confuso el código.",
            ),
            (
                "Usar == en vez de is con None",
                "Para comprobar ausencia de valor usa `is None`.",
            ),
            (
                "Mutables como default en funciones",
                "Listas o dicts como valores por defecto se comparten entre llamadas.",
            ),
            (
                "Crear listas con *",
                "[[0]] * 3 repite referencias: modificar un elemento afecta a todos.",
            ),
            (
                "Olvidar que str es inmutable",
                "Métodos como upper devuelven un nuevo texto; no modifican el original.",
            ),
            (
                "Nombrar variables como list o dict",
                "Sobrescribes funciones útiles del lenguaje y pierdes acceso a ellas.",
            ),
            (
                "Confundir 0 con None",
                "0 puede ser un valor válido; None indica ausencia de valor.",
            ),
            (
                "No convertir antes de concatenar",
                "Concatenar texto y números sin str() produce errores de tipo.",
            ),
            (
                "Asumir que copy() duplica todo",
                "copy() no copia listas internas; usa copy profundo cuando haya anidaciones.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Crear variables con sentido",
                """# Aprende esto
# Aprenderás a guardar datos con nombres claros.
# Verás cómo reutilizar valores para construir mensajes.
#
# Haz esto
nombre = "Ana"  # Guardamos el nombre como texto
apellido = "López"  # Guardamos el apellido
nombre_completo = nombre + " " + apellido  # Unimos nombre y apellido
etiqueta = "Cliente"  # Definimos un rol descriptivo
mensaje = etiqueta + ": " + nombre_completo  # Construimos un mensaje final
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás un texto con el formato "Cliente: Ana López".
#
# Por qué funciona
# Cada variable apunta a un string y el operador + concatena esos textos.
#
# Lo típico que sale mal
# - Usar nombres genéricos como x o tmp y perder significado.
# - Olvidar el espacio entre nombre y apellido.
""",
            ),
            (
                "Tipos básicos y conversión",
                """# Aprende esto
# Aprenderás a distinguir int, float y str.
# Verás cómo convertir un número a texto para mostrarlo.
#
# Haz esto
edad = 20  # Guardamos un entero
altura = 1.72  # Guardamos un decimal
texto_edad = str(edad)  # Convertimos el entero a texto
mensaje = "Edad: " + texto_edad  # Construimos un mensaje con texto
print(mensaje)  # Mostramos el mensaje
print(altura + 0.03)  # Sumamos decimales
#
# Verás esto
# Verás "Edad: 20" y un decimal como 1.75.
#
# Por qué funciona
# str() convierte el entero y los floats permiten operaciones con decimales.
#
# Lo típico que sale mal
# - Concatenar texto y número sin str().
# - Usar coma en lugar de punto en decimales.
""",
            ),
            (
                "Tipado dinámico controlado",
                """# Aprende esto
# Aprenderás a cambiar de tipo de forma explícita.
# Verás por qué conviene hacerlo al final del flujo.
#
# Haz esto
valor = 10  # Empezamos con un entero
valor = valor + 5  # Sumamos otro entero
texto_valor = str(valor)  # Convertimos el resultado a texto
etiqueta = "Total"  # Creamos un texto descriptivo
mensaje = etiqueta + ": " + texto_valor  # Combinamos etiqueta y valor
print(mensaje)  # Mostramos el resultado
#
# Verás esto
# Verás "Total: 15" como salida.
#
# Por qué funciona
# Primero operamos con int y luego convertimos para mostrar.
#
# Lo típico que sale mal
# - Cambiar el tipo a mitad del cálculo.
# - Reutilizar la misma variable con tipos distintos.
""",
            ),
            (
                "Lista mutable con append",
                """# Aprende esto
# Aprenderás que las listas cambian en el mismo objeto.
# Verás cómo append agrega elementos sin crear otra lista.
#
# Haz esto
compras = ["pan", "leche"]  # Lista inicial
compras.append("café")  # Agregamos un nuevo elemento
compras.append("azúcar")  # Agregamos otro elemento
conteo = len(compras)  # Contamos elementos actuales
print(compras)  # Mostramos la lista completa
print(conteo)  # Mostramos la cantidad
#
# Verás esto
# Verás la lista con cuatro elementos y el número 4.
#
# Por qué funciona
# append modifica la lista original y len cuenta elementos actuales.
#
# Lo típico que sale mal
# - Creer que append devuelve una lista nueva.
# - Olvidar que la lista se modifica en sitio.
""",
            ),
            (
                "String inmutable con upper",
                """# Aprende esto
# Aprenderás que los strings no se modifican en sitio.
# Verás cómo crear una nueva variable con el resultado.
#
# Haz esto
texto = "hola"  # String original
texto_mayus = texto.upper()  # upper crea un nuevo string
texto_limpio = texto.strip()  # strip devuelve otro string
resumen = texto + " -> " + texto_mayus  # Creamos un resumen
print(texto)  # Mostramos el original
print(resumen)  # Mostramos el cambio
#
# Verás esto
# Verás el original en minúsculas y el resumen con mayúsculas.
#
# Por qué funciona
# upper y strip devuelven nuevos strings porque los strings son inmutables.
#
# Lo típico que sale mal
# - Esperar que upper cambie el original.
# - No guardar el resultado en otra variable.
""",
            ),
            (
                "Alias vs copia",
                """# Aprende esto
# Aprenderás la diferencia entre alias y copia real.
# Verás cómo evitar cambios inesperados en listas.
#
# Haz esto
original = [1, 2]  # Lista original
alias = original  # Alias al mismo objeto
alias.append(3)  # Modificamos la lista original
copia = original.copy()  # Copia superficial independiente
copia.append(99)  # Solo cambia la copia
print(original)  # Mostramos la lista original
#
# Verás esto
# Verás [1, 2, 3] y no verás el 99 en la lista original.
#
# Por qué funciona
# alias apunta al mismo objeto y copy() crea una nueva lista.
#
# Lo típico que sale mal
# - Pensar que b = a crea una copia.
# - Modificar un alias sin querer.
""",
            ),
            (
                "Conversión explícita y uso de None",
                """# Aprende esto
# Aprenderás a convertir texto numérico a entero.
# Verás cómo usar None para indicar ausencia de valor.
#
# Haz esto
texto = "42"  # Texto numérico
numero = int(texto)  # Convertimos a entero
resultado = None  # Aún no hay resultado
resultado = numero + 8  # Calculamos un valor final
if resultado is not None:  # Comprobamos que existe
    print(resultado)  # Mostramos el resultado
#
# Verás esto
# Verás el número 50 en pantalla.
#
# Por qué funciona
# int() convierte texto a entero y None indica ausencia de valor.
#
# Lo típico que sale mal
# - Comparar con None usando == en lugar de is.
# - Asumir que None equivale a 0.
""",
            ),
            (
                "Longitud con len",
                """# Aprende esto
# Aprenderás a contar elementos en una lista.
# Verás cómo guardar ese conteo para reutilizarlo.
#
# Haz esto
datos = ["a", "b", "c"]  # Lista con tres elementos
cantidad = len(datos)  # len devuelve la cantidad de elementos
mensaje = "Total: " + str(cantidad)  # Convertimos para mostrar
print(mensaje)  # Mostramos el mensaje
print(datos)  # Mostramos la lista completa
#
# Verás esto
# Verás "Total: 3" y la lista con tres letras.
#
# Por qué funciona
# len cuenta elementos y str permite concatenar con texto.
#
# Lo típico que sale mal
# - Olvidar convertir el número a texto.
# - Confundir len con el último índice.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una variable llamada ciudad con el valor 'Lima' y muéstrala.",
                "hints": ["Usa print"],
                "solution": "ciudad = 'Lima'\nprint(ciudad)",
            },
            {
                "question": "Convierte la cadena '3.14' a float y súmale 1.",
                "hints": ["Usa float()"],
                "solution": "valor = float('3.14')\nprint(valor + 1)",
            },
            {
                "question": "Crea una lista con tres frutas y agrega una cuarta con append.",
                "hints": ["Lista con []", "append agrega al final"],
                "solution": "frutas = ['manzana', 'pera', 'uva']\nfrutas.append('naranja')\nprint(frutas)",
            },
            {
                "question": "Demuestra que una copia de lista no cambia al modificar la copia.",
                "hints": ["Usa copy()"],
                "solution": "original = [1, 2]\ncopia = original.copy()\ncopia.append(3)\nprint(original)",
            },
            {
                "question": "Guarda None en una variable llamada resultado y compruébalo con is.",
                "hints": ["Usa if"],
                "solution": "resultado = None\nif resultado is None:\n    print('Sin resultado')",
            },
            {
                "question": "Convierte un entero a texto y concaténalo en un mensaje.",
                "hints": ["Usa str()"],
                "solution": "edad = 30\nmensaje = 'Edad: ' + str(edad)\nprint(mensaje)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget

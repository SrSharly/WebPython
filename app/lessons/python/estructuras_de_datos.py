from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class EstructurasDeDatosLesson(Lesson):
    TITLE = "Estructuras de datos"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["listas", "tuplas", "diccionarios", "sets"]

    def summary(self) -> str:
        return (
            "Aprende qué estructura de datos usar en cada caso: listas para orden, tuplas para "
            "inmutabilidad, diccionarios para pares clave-valor y sets para unicidad."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: elegir bien la estructura evita errores
Las estructuras de datos te permiten **organizar información**. Elegir la correcta ahorra tiempo y previene errores:
una lista es ideal para mantener orden, un diccionario para buscar por clave y un set para eliminar duplicados.
En este tutorial aprenderás cuándo usar cada una y cómo trabajar con ellas paso a paso.

## Paso 1: Listas para orden y modificación
Las listas guardan elementos en orden y permiten agregar o eliminar elementos.

**Aprende esto**
- Aprenderás a crear listas y modificarlas con métodos simples.
- Verás cómo el orden se mantiene y cómo contar elementos.

**Haz esto**
```
compras = ["pan", "leche"]  # Creamos una lista ordenada
compras.append("café")  # Agregamos un elemento al final
compras.insert(1, "huevos")  # Insertamos en una posición específica
cantidad = len(compras)  # Contamos elementos
print(compras)  # Mostramos la lista actual
print(cantidad)  # Mostramos la cantidad
```

**Verás esto**
Verás la lista en el orden correcto y la cantidad total.

**Por qué funciona**
`append` agrega al final e `insert` respeta posiciones. `len` cuenta los elementos actuales.

**Lo típico que sale mal**
- Confundir `append` con `extend` y agregar una lista completa sin querer.
- Usar índices fuera de rango.

## Paso 2: Tuplas para datos fijos
Una tupla es como una lista pero **inmutable**: no se puede modificar.

**Aprende esto**
- Aprenderás a usar tuplas para datos que no deben cambiar.
- Verás cómo desempaquetar tuplas en variables.

**Haz esto**
```
coordenadas = (10, 20)  # Tupla con dos valores
x, y = coordenadas  # Desempaquetamos la tupla
mensaje = "X=" + str(x)  # Convertimos para mostrar
mensaje += " Y=" + str(y)  # Construimos un texto final
print(mensaje)  # Mostramos el resultado
```

**Verás esto**
Verás un texto como `X=10 Y=20`.

**Por qué funciona**
Las tuplas preservan el orden y permiten desempaquetar sus valores de forma directa.

**Lo típico que sale mal**
- Intentar modificar una tupla con `append`.
- Desempaquetar con un número incorrecto de variables.

## Paso 3: Diccionarios para clave-valor
Un diccionario conecta una **clave** con un **valor**. Es ideal para buscar rápido por nombre o ID.

**Aprende esto**
- Aprenderás a crear diccionarios y actualizar valores por clave.
- Verás cómo acceder a datos sin recorrer toda la estructura.

**Haz esto**
```
cliente = {"nombre": "Ana", "edad": 30}  # Diccionario inicial
cliente["edad"] = 31  # Actualizamos un valor por clave
cliente["ciudad"] = "Lima"  # Agregamos una nueva clave
resumen = cliente["nombre"] + " - " + cliente["ciudad"]  # Leemos datos
print(resumen)  # Mostramos el resumen
```

**Verás esto**
Verás un resumen como `Ana - Lima`.

**Por qué funciona**
Las claves permiten acceder a valores específicos sin depender del orden.

**Lo típico que sale mal**
- Acceder a una clave inexistente y generar `KeyError`.
- Usar listas como claves (no son válidas porque son mutables).

## Paso 4: Sets para unicidad
Un set guarda elementos **sin duplicados** y no mantiene orden.

**Aprende esto**
- Aprenderás a eliminar duplicados usando sets.
- Verás operaciones básicas como agregar y comprobar pertenencia.

**Haz esto**
```
ciudades = ["Lima", "Cusco", "Lima", "Arequipa"]  # Lista con duplicados
unicas = set(ciudades)  # Convertimos a set para eliminar duplicados
unicas.add("Piura")  # Agregamos un elemento nuevo
hay_lima = "Lima" in unicas  # Comprobamos pertenencia
print(unicas)  # Mostramos el set
print(hay_lima)  # Mostramos True
```

**Verás esto**
Verás un set con elementos únicos y `True` indicando que Lima está presente.

**Por qué funciona**
Un set no permite duplicados y el operador `in` verifica pertenencia rápidamente.

**Lo típico que sale mal**
- Esperar que el set mantenga el orden original.
- Convertir a set y luego intentar indexarlo.

## Paso 5: Elegir la estructura correcta
Elige según la necesidad: orden, clave-valor o unicidad.

**Aprende esto**
- Aprenderás a justificar la estructura según el problema.
- Verás cómo combinar estructuras para resolver casos reales.

**Haz esto**
```
ventas = [120, 200, 150]  # Lista de montos ordenados
cliente = {"id": 1, "nombre": "Ana"}  # Diccionario con datos del cliente
productos = {"pan", "leche", "café"}  # Set de productos únicos
promedio = sum(ventas) / len(ventas)  # Calculamos promedio
resumen = cliente["nombre"] + " compra " + str(len(productos)) + " productos"  # Texto
print(promedio)  # Mostramos el promedio
print(resumen)  # Mostramos el resumen
```

**Verás esto**
Verás un promedio numérico y un texto indicando cuántos productos únicos hay.

**Por qué funciona**
Cada estructura se usa en lo que mejor hace: listas para orden, dict para datos del cliente, set para unicidad.

**Lo típico que sale mal**
- Usar lista cuando necesitas búsqueda rápida por clave.
- Usar dict cuando solo necesitas una colección ordenada.

## Más allá (nivel pro)
Puedes combinar estructuras para modelar datos reales sin depender de una base de datos.

**Aprende esto**
- Aprenderás a usar listas de diccionarios para datos tabulares.
- Verás cómo filtrar y resumir con claridad.

**Haz esto**
```
clientes = [
    {"id": 1, "nombre": "Ana"},  # Primer cliente
    {"id": 2, "nombre": "Luis"},  # Segundo cliente
]  # Lista de diccionarios
ids = {cliente["id"] for cliente in clientes}  # Set de ids únicos
nombres = [cliente["nombre"] for cliente in clientes]  # Lista de nombres
print(ids)  # Mostramos ids únicos
print(nombres)  # Mostramos los nombres
```

**Verás esto**
Verás un set con ids y una lista con nombres.

**Por qué funciona**
Las comprensiones recorren la lista y extraen la información más relevante de cada diccionario.

**Lo típico que sale mal**
- Olvidar que un set no preserva orden.
- Usar claves incorrectas dentro del diccionario.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Confundir append y extend",
                "append agrega un elemento; extend agrega todos los elementos de otra lista.",
            ),
            (
                "Índices fuera de rango",
                "Acceder a una posición inexistente en una lista genera IndexError.",
            ),
            (
                "Modificar una tupla",
                "Las tuplas son inmutables; no permiten append ni asignación por índice.",
            ),
            (
                "KeyError en diccionarios",
                "Acceder a una clave inexistente genera un error. Usa get si no estás seguro.",
            ),
            (
                "Usar listas como claves",
                "Las listas son mutables y no se pueden usar como claves en dict.",
            ),
            (
                "Esperar orden en sets",
                "Los sets no mantienen orden y no pueden indexarse.",
            ),
            (
                "Duplicados en listas",
                "Si necesitas unicidad, usa set o elimina duplicados.",
            ),
            (
                "Confundir lista y tupla",
                "La tupla se usa para datos que no deben cambiar.",
            ),
            (
                "No copiar listas anidadas",
                "Una copia superficial no separa listas internas.",
            ),
            (
                "Usar dict cuando solo necesitas orden",
                "Si no necesitas claves, una lista suele ser más simple.",
            ),
            (
                "Olvidar convertir a list",
                "Si necesitas ordenar un set, primero conviértelo a lista.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Lista con append e insert",
                """# Aprende esto
# Aprenderás a mantener el orden en una lista.
# Verás cómo agregar elementos en posiciones específicas.
#
# Haz esto
compras = ["pan", "leche"]  # Lista inicial
compras.append("café")  # Agregamos al final
compras.insert(1, "huevos")  # Insertamos en la posición 1
cantidad = len(compras)  # Contamos elementos
print(compras)  # Mostramos la lista
print(cantidad)  # Mostramos la cantidad
#
# Verás esto
# Verás la lista con huevos en la posición 1.
#
# Por qué funciona
# append agrega al final e insert inserta en la posición indicada.
#
# Lo típico que sale mal
# - Confundir append con extend.
# - Usar índices inválidos.
""",
            ),
            (
                "Tupla inmutable",
                """# Aprende esto
# Aprenderás a usar tuplas para datos fijos.
# Verás cómo desempaquetar valores.
#
# Haz esto
coordenadas = (10, 20)  # Tupla con dos números
x, y = coordenadas  # Desempaquetamos en dos variables
mensaje = "X=" + str(x)  # Construimos el texto
mensaje += " Y=" + str(y)  # Añadimos el segundo valor
print(mensaje)  # Mostramos el resultado
#
# Verás esto
# Verás "X=10 Y=20".
#
# Por qué funciona
# Las tuplas preservan el orden y permiten desempaquetar.
#
# Lo típico que sale mal
# - Intentar modificar la tupla.
# - Desempaquetar con variables de más o de menos.
""",
            ),
            (
                "Diccionario básico",
                """# Aprende esto
# Aprenderás a usar claves para acceder a valores.
# Verás cómo actualizar un diccionario.
#
# Haz esto
cliente = {"nombre": "Ana", "edad": 30}  # Diccionario inicial
cliente["edad"] = 31  # Actualizamos la edad
cliente["ciudad"] = "Lima"  # Agregamos una nueva clave
resumen = cliente["nombre"] + " - " + cliente["ciudad"]  # Resumen
print(resumen)  # Mostramos el resumen
#
# Verás esto
# Verás "Ana - Lima".
#
# Por qué funciona
# Las claves permiten acceder directamente a los valores.
#
# Lo típico que sale mal
# - Acceder a claves que no existen.
# - Usar claves mutables.
""",
            ),
            (
                "Set sin duplicados",
                """# Aprende esto
# Aprenderás a eliminar duplicados con un set.
# Verás cómo comprobar pertenencia.
#
# Haz esto
ciudades = ["Lima", "Cusco", "Lima", "Arequipa"]  # Lista con duplicados
unicas = set(ciudades)  # Eliminamos duplicados
unicas.add("Piura")  # Agregamos otra ciudad
hay_lima = "Lima" in unicas  # Verificamos pertenencia
print(unicas)  # Mostramos el set
print(hay_lima)  # Mostramos True
#
# Verás esto
# Verás un set con elementos únicos.
#
# Por qué funciona
# Los sets no permiten duplicados y "in" es rápido.
#
# Lo típico que sale mal
# - Esperar orden en un set.
# - Intentar indexar un set.
""",
            ),
            (
                "Combinar estructuras",
                """# Aprende esto
# Aprenderás a usar varias estructuras en un mismo flujo.
# Verás cómo cada una aporta algo distinto.
#
# Haz esto
ventas = [120, 200, 150]  # Lista de ventas
cliente = {"nombre": "Ana"}  # Diccionario con datos
productos = {"pan", "leche", "café"}  # Set de productos
promedio = sum(ventas) / len(ventas)  # Calculamos promedio
resumen = cliente["nombre"] + " compra " + str(len(productos)) + " productos"  # Texto
print(promedio)  # Mostramos el promedio
print(resumen)  # Mostramos el resumen
#
# Verás esto
# Verás un promedio y un resumen del cliente.
#
# Por qué funciona
# Cada estructura se usa según su ventaja principal.
#
# Lo típico que sale mal
# - Usar dict cuando basta una lista.
# - No convertir números a texto al concatenar.
""",
            ),
            (
                "Comprensión de listas",
                """# Aprende esto
# Aprenderás a transformar datos con comprensión.
# Verás cómo crear una lista nueva fácilmente.
#
# Haz esto
precios = [10, 20, 30]  # Lista original
precios_con_impuesto = [precio * 1.18 for precio in precios]  # Calculamos
cantidad = len(precios_con_impuesto)  # Contamos elementos
print(precios_con_impuesto)  # Mostramos la lista nueva
print(cantidad)  # Mostramos la cantidad
#
# Verás esto
# Verás una lista con precios aumentados.
#
# Por qué funciona
# La comprensión recorre la lista y crea otra con el cálculo.
#
# Lo típico que sale mal
# - Usar comprensión sin leerla con calma.
# - Olvidar que crea una lista nueva.
""",
            ),
            (
                "Diccionario con get",
                """# Aprende esto
# Aprenderás a evitar KeyError usando get.
# Verás cómo definir un valor por defecto.
#
# Haz esto
config = {"debug": True}  # Diccionario de configuración
modo = config.get("modo", "producción")  # Valor por defecto
activo = config.get("debug", False)  # Leemos una clave existente
print(modo)  # Mostramos el modo
print(activo)  # Mostramos el estado de debug
#
# Verás esto
# Verás "producción" y True.
#
# Por qué funciona
# get devuelve el default si la clave no existe.
#
# Lo típico que sale mal
# - Acceder directamente a claves inexistentes.
# - Olvidar un default adecuado.
""",
            ),
            (
                "Set para deduplicar",
                """# Aprende esto
# Aprenderás a quitar duplicados rápidamente.
# Verás cómo volver a lista si necesitas orden.
#
# Haz esto
nombres = ["Ana", "Luis", "Ana", "Marta"]  # Lista con repetidos
unicos = set(nombres)  # Quitamos duplicados
lista_unicos = list(unicos)  # Convertimos a lista
cantidad = len(lista_unicos)  # Contamos elementos
print(lista_unicos)  # Mostramos la lista resultante
print(cantidad)  # Mostramos la cantidad
#
# Verás esto
# Verás una lista sin duplicados.
#
# Por qué funciona
# set elimina duplicados y list permite trabajar con índices.
#
# Lo típico que sale mal
# - Esperar que se conserve el orden original.
# - Olvidar que set no es indexable.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una lista de tareas y agrega una nueva tarea al final.",
                "hints": ["Usa append"],
                "solution": "tareas = ['leer', 'estudiar']\ntareas.append('practicar')\nprint(tareas)",
            },
            {
                "question": "Define una tupla con dos coordenadas y muéstralas en un mensaje.",
                "hints": ["Usa desempaquetado"],
                "solution": "coord = (5, 8)\nx, y = coord\nprint('X=' + str(x) + ' Y=' + str(y))",
            },
            {
                "question": "Crea un diccionario con nombre y edad y actualiza la edad.",
                "hints": ["Usa clave 'edad'"],
                "solution": "persona = {'nombre': 'Ana', 'edad': 20}\npersona['edad'] = 21\nprint(persona)",
            },
            {
                "question": "Elimina duplicados de una lista usando set.",
                "hints": ["Convierte la lista a set"],
                "solution": "nombres = ['Ana', 'Luis', 'Ana']\nunicos = set(nombres)\nprint(unicos)",
            },
            {
                "question": "Calcula el promedio de una lista de números.",
                "hints": ["Usa sum() y len()"],
                "solution": "numeros = [10, 20, 30]\npromedio = sum(numeros) / len(numeros)\nprint(promedio)",
            },
            {
                "question": "Usa get en un diccionario para evitar KeyError.",
                "hints": ["Define un valor por defecto"],
                "solution": "config = {'debug': True}\nmodo = config.get('modo', 'prod')\nprint(modo)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget

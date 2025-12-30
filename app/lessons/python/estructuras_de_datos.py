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
            "Aprende desde cero cómo usar listas, tuplas, diccionarios y sets para organizar datos, "
            "con ejemplos claros y errores comunes explicados."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: datos bien organizados, decisiones más fáciles
Las estructuras de datos son contenedores con reglas claras. Una lista mantiene orden, una tupla asegura inmutabilidad,
un diccionario relaciona claves con valores y un set guarda únicos. Elegir bien la estructura evita bugs, hace el código
más corto y te ayuda a razonar con claridad. Este tutorial te guía desde cero para que sepas cuándo usar cada una.

## Paso 1: Listas para colecciones ordenadas
Las listas son ideales cuando necesitas mantener un orden y modificar elementos.

**Aprende esto**
- Aprenderás a crear listas y agregar elementos de forma segura.
- Verás cómo leer elementos por índice y contar el total.

**Haz esto**
print("ok")  # Confirmamos
```
frutas = ["manzana", "pera", "uva"]  # Lista ordenada
frutas.append("naranja")  # Agregamos un elemento al final
primera = frutas[0]  # Leemos el primer elemento
ultima = frutas[-1]  # Leemos el último elemento
cantidad = len(frutas)  # Contamos elementos
resumen = "Primera: " + primera + ", Última: " + ultima  # Resumen
print(frutas)  # Mostramos la lista completa
print(resumen)  # Mostramos el resumen
print(cantidad)  # Mostramos la cantidad
print("ok")  # Confirmamos
```

**Verás esto**
Verás la lista con cuatro frutas, un resumen de primera y última, y el número 4.

**Por qué funciona**
Las listas mantienen orden, permiten índices positivos y negativos, y `len()` devuelve la cantidad actual.

**Lo típico que sale mal**
- Acceder a un índice fuera del rango y provocar un error.
- Olvidar que `append()` modifica la lista en sitio.

## Paso 2: Tuplas para datos fijos
Las tuplas son colecciones ordenadas pero inmutables. Úsalas cuando el dato no debe cambiar.

**Aprende esto**
- Aprenderás a crear tuplas y a usarlas para datos constantes.
- Verás cómo desempaquetar valores de una tupla.

**Haz esto**
print("ok")  # Confirmamos
```
coordenadas = (10, 20)  # Tupla con dos valores
x, y = coordenadas  # Desempaquetamos en variables
mensaje = "X: " + str(x) + ", Y: " + str(y)  # Construimos un mensaje
print(coordenadas)  # Mostramos la tupla
print(mensaje)  # Mostramos el mensaje
print(type(coordenadas))  # Confirmamos el tipo
print(len(coordenadas))  # Contamos elementos
print("ok")  # Confirmamos
```

**Verás esto**
Verás `(10, 20)`, el mensaje y el tipo `<class 'tuple'>`.

**Por qué funciona**
Las tuplas mantienen el orden, se pueden desempaquetar y no permiten modificaciones en sitio.

**Lo típico que sale mal**
- Intentar usar `append()` en una tupla.
- Olvidar el orden al desempaquetar.

## Paso 3: Diccionarios para datos con clave
Los diccionarios relacionan una clave con un valor, perfectos para datos tipo ficha.

**Aprende esto**
- Aprenderás a crear diccionarios y acceder por clave.
- Verás cómo agregar nuevas claves de forma segura.

**Haz esto**
print("ok")  # Confirmamos
```
cliente = {"nombre": "Ana", "edad": 30}  # Diccionario base
cliente["ciudad"] = "Lima"  # Agregamos una nueva clave
nombre = cliente["nombre"]  # Accedemos a una clave
edad = cliente.get("edad", 0)  # Leemos con valor por defecto
resumen = nombre + " - " + str(edad)  # Creamos un resumen
print(cliente)  # Mostramos el diccionario
print(resumen)  # Mostramos el resumen
print(len(cliente))  # Mostramos cuántas claves hay
print("ok")  # Confirmamos
```

**Verás esto**
Verás el diccionario con tres claves y un resumen como `Ana - 30`.

**Por qué funciona**
Los diccionarios mapean claves únicas a valores. `get()` evita errores si la clave no existe.

**Lo típico que sale mal**
- Acceder a una clave inexistente con `[]` y obtener un error.
- Usar claves mutables como listas (no son válidas).

## Paso 4: Sets para valores únicos
Los sets guardan valores sin duplicados y no garantizan orden.

**Aprende esto**
- Aprenderás a usar sets para eliminar duplicados.
- Verás operaciones básicas como agregar y comprobar pertenencia.

**Haz esto**
print("ok")  # Confirmamos
```
valores = ["rojo", "azul", "rojo", "verde"]  # Lista con duplicados
colores = set(valores)  # Convertimos a set para únicos
colores.add("amarillo")  # Agregamos un nuevo color
hay_rojo = "rojo" in colores  # Verificamos pertenencia
cantidad = len(colores)  # Contamos elementos únicos
print(colores)  # Mostramos el set
print(hay_rojo)  # Mostramos el resultado de la búsqueda
print(cantidad)  # Mostramos la cantidad de únicos
print("ok")  # Confirmamos
```

**Verás esto**
Verás un set con colores únicos, `True` para la pertenencia y la cantidad total.

**Por qué funciona**
Los sets eliminan duplicados automáticamente y permiten operaciones rápidas de pertenencia.

**Lo típico que sale mal**
- Esperar un orden fijo en el set.
- Intentar acceder por índice como si fuera una lista.

## Paso 5: Estructuras anidadas
En proyectos reales, combinas estructuras: listas de diccionarios, diccionarios con listas, etc.

**Aprende esto**
- Aprenderás a mezclar estructuras para representar datos reales.
- Verás cómo acceder a datos anidados con claridad.

**Haz esto**
print("ok")  # Confirmamos
```
ventas = [  # Lista de diccionarios
    {"producto": "A", "monto": 100},  # Venta 1
    {"producto": "B", "monto": 150},  # Venta 2
]  # Cerramos la lista
monto_total = ventas[0]["monto"] + ventas[1]["monto"]  # Sumamos montos
producto_primero = ventas[0]["producto"]  # Leemos el primer producto
resumen = producto_primero + " y total " + str(monto_total)  # Resumen
print(ventas)  # Mostramos la estructura
print(resumen)  # Mostramos el resumen
print(len(ventas))  # Mostramos la cantidad de ventas
print("ok")  # Confirmamos
```

**Verás esto**
Verás la lista de ventas y un resumen como `A y total 250`.

**Por qué funciona**
Una lista mantiene orden de ventas, y cada diccionario permite acceder por clave a los datos de cada venta.

**Lo típico que sale mal**
- Confundir índices y claves al acceder a datos anidados.
- Modificar la estructura sin validar sus niveles.

## Paso 6: Elegir la estructura correcta
La estructura correcta reduce código y errores: listas para secuencias, tuplas para datos fijos, diccionarios para
atributos y sets para únicos.

**Aprende esto**
- Aprenderás a comparar estructuras y elegir la mejor para cada caso.
- Verás cómo documentar esa elección con nombres claros.

**Haz esto**
print("ok")  # Confirmamos
```
usuarios = ["Ana", "Luis", "Ana"]  # Lista con duplicados
usuarios_unicos = set(usuarios)  # Quitamos duplicados
perfil = {"nombre": "Ana", "rol": "admin"}  # Diccionario de atributos
coordenadas = (12, 8)  # Tupla fija con dos valores
resumen = perfil["nombre"] + " en " + str(coordenadas)  # Resumen
print(usuarios_unicos)  # Mostramos usuarios únicos
print(perfil)  # Mostramos el perfil
print(resumen)  # Mostramos el resumen
print("ok")  # Confirmamos
```

**Verás esto**
Verás un set con usuarios únicos, el diccionario de perfil y el resumen con coordenadas.

**Por qué funciona**
Cada estructura cumple un rol: eliminar duplicados, guardar atributos y mantener pares fijos.

**Lo típico que sale mal**
- Usar listas cuando necesitas acceso por clave (diccionario sería mejor).
- Usar sets cuando el orden sí importa.

## Más allá (nivel pro): comprensiones y copias
Las comprensiones permiten construir colecciones en una línea legible y las copias evitan efectos secundarios.

**Aprende esto**
- Aprenderás a crear listas y diccionarios nuevos con comprensiones.
- Verás cómo copiar estructuras para no modificar el original.

**Haz esto**
print("ok")  # Confirmamos
```
precios = [10, 20, 30]  # Lista base
precios_con_iva = [p * 1.18 for p in precios]  # Nueva lista calculada
indice = {p: p * 1.18 for p in precios}  # Diccionario con precios y total
copia_precios = precios.copy()  # Copia superficial
copia_precios.append(40)  # Modificamos solo la copia
print(precios)  # Mostramos la lista original
print(precios_con_iva)  # Mostramos la lista calculada
print(indice)  # Mostramos el diccionario
print("ok")  # Confirmamos
```

**Verás esto**
Verás la lista original intacta, una nueva lista con IVA y un diccionario con los valores calculados.

**Por qué funciona**
Las comprensiones generan nuevas colecciones sin modificar la original. `copy()` crea una lista independiente.

**Lo típico que sale mal**
- Creer que la comprensión modifica la lista original.
- Usar `copy()` en estructuras anidadas sin considerar copias profundas.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Índices fuera de rango",
                "Acceder a posiciones inexistentes en listas produce errores.",
            ),
            (
                "Modificar tuplas",
                "Las tuplas son inmutables; no permiten append ni asignación.",
            ),
            (
                "Usar claves inexistentes",
                "Acceder con [] a una clave inexistente lanza KeyError.",
            ),
            (
                "Confundir set con lista",
                "Los sets no mantienen orden ni permiten índices.",
            ),
            (
                "Olvidar copy()",
                "Asignar b = a en listas crea alias, no copia.",
            ),
            (
                "Usar listas como claves",
                "Las claves de diccionario deben ser inmutables.",
            ),
            (
                "No validar niveles anidados",
                "Acceder a estructuras anidadas sin revisar su forma causa errores.",
            ),
            (
                "Esperar orden en sets",
                "El orden de un set puede cambiar entre ejecuciones.",
            ),
            (
                "Confundir list y dict",
                "Listas usan índices; diccionarios usan claves.",
            ),
            (
                "No usar get()",
                "get() evita errores cuando una clave puede faltar.",
            ),
            (
                "Sobrescribir datos",
                "Asignar la misma clave en un dict reemplaza el valor anterior.",
            ),
            (
                "Duplicar datos con comprensiones",
                "Si no filtras correctamente, puedes crear colecciones innecesarias.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "Lista ordenada básica",
                """# Aprende esto
# Aprenderás a crear una lista y agregar elementos.
# Verás cómo acceder a elementos por índice.
# Practicarás el conteo con len.
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista inicial
frutas.append("naranja")  # Agregamos una fruta
primera = frutas[0]  # Leemos el primer elemento
ultima = frutas[-1]  # Leemos el último elemento
cantidad = len(frutas)  # Contamos elementos
resumen = "Primera: " + primera + ", Última: " + ultima  # Resumen
print(frutas)  # Mostramos la lista
print(resumen)  # Mostramos el resumen
print(cantidad)  # Mostramos la cantidad
#
# Verás esto
# Verás la lista con cuatro elementos y un resumen.
#
# Por qué funciona
# Las listas mantienen orden y len cuenta elementos.
#
# Lo típico que sale mal
# - Acceder a índices fuera de rango.
# - Creer que append devuelve una nueva lista.
""",
            ),
            (
                "Tupla fija con desempaquetado",
                """# Aprende esto
# Aprenderás a usar tuplas para datos fijos.
# Verás cómo desempaquetar valores.
# Confirmarás el tipo con type().
#
# Haz esto
coordenadas = (10, 20)  # Tupla con dos valores
x, y = coordenadas  # Desempaquetamos
total = x + y  # Sumamos valores
mensaje = "X: " + str(x) + ", Y: " + str(y)  # Mensaje
print(coordenadas)  # Mostramos la tupla
print(mensaje)  # Mostramos el mensaje
print(total)  # Mostramos la suma
print(type(coordenadas))  # Confirmamos el tipo
print(len(coordenadas))  # Contamos elementos
#
# Verás esto
# Verás la tupla, el mensaje y el tipo tuple.
#
# Por qué funciona
# Las tuplas son inmutables y se pueden desempaquetar.
#
# Lo típico que sale mal
# - Intentar usar append en una tupla.
# - Olvidar el orden de los valores.
""",
            ),
            (
                "Diccionario con claves",
                """# Aprende esto
# Aprenderás a crear un diccionario y leer claves.
# Verás cómo agregar nuevas claves.
# Evitarás errores con get().
#
# Haz esto
cliente = {"nombre": "Ana", "edad": 30}  # Diccionario base
cliente["ciudad"] = "Lima"  # Agregamos ciudad
nombre = cliente["nombre"]  # Leemos nombre
edad = cliente.get("edad", 0)  # Leemos con default
resumen = nombre + " - " + str(edad)  # Resumen
print(cliente)  # Mostramos el dict
print(resumen)  # Mostramos el resumen
print(len(cliente))  # Contamos claves
#
# Verás esto
# Verás el diccionario con tres claves y el resumen.
#
# Por qué funciona
# Las claves apuntan a valores y get evita errores si falta una clave.
#
# Lo típico que sale mal
# - Acceder a una clave inexistente con [].
# - Usar claves mutables.
""",
            ),
            (
                "Set para eliminar duplicados",
                """# Aprende esto
# Aprenderás a usar sets para únicos.
# Verás cómo agregar y comprobar pertenencia.
# Entenderás que no hay orden garantizado.
#
# Haz esto
valores = ["rojo", "azul", "rojo", "verde"]  # Lista con duplicados
colores = set(valores)  # Convertimos a set
colores.add("amarillo")  # Agregamos color
hay_rojo = "rojo" in colores  # Verificamos pertenencia
cantidad = len(colores)  # Contamos elementos
print(colores)  # Mostramos el set
print(hay_rojo)  # Mostramos el booleano
print(cantidad)  # Mostramos la cantidad
#
# Verás esto
# Verás colores únicos, True y la cantidad total.
#
# Por qué funciona
# El set elimina duplicados y permite búsquedas rápidas.
#
# Lo típico que sale mal
# - Esperar orden fijo.
# - Intentar usar índices.
""",
            ),
            (
                "Lista de diccionarios",
                """# Aprende esto
# Aprenderás a combinar estructuras para datos reales.
# Verás cómo acceder a claves dentro de una lista.
# Evitarás confundir índices y claves.
#
# Haz esto
ventas = [  # Lista de diccionarios
    {"producto": "A", "monto": 100},  # Venta 1
    {"producto": "B", "monto": 150},  # Venta 2
]  # Cerramos la lista
monto_total = ventas[0]["monto"] + ventas[1]["monto"]  # Sumamos
producto_primero = ventas[0]["producto"]  # Primer producto
resumen = producto_primero + " y total " + str(monto_total)  # Resumen
print(ventas)  # Mostramos estructura
print(resumen)  # Mostramos resumen
print(len(ventas))  # Contamos ventas
#
# Verás esto
# Verás la lista de ventas y el resumen con total.
#
# Por qué funciona
# La lista mantiene orden y cada dict guarda datos por clave.
#
# Lo típico que sale mal
# - Mezclar índices con claves.
# - Asumir que todas las ventas tienen las mismas claves.
""",
            ),
            (
                "Seleccionar estructura adecuada",
                """# Aprende esto
# Aprenderás a elegir la estructura según la necesidad.
# Verás un ejemplo que combina varias estructuras.
# Reducirás errores al modelar datos.
#
# Haz esto
usuarios = ["Ana", "Luis", "Ana"]  # Lista con duplicados
usuarios_unicos = set(usuarios)  # Eliminamos duplicados
perfil = {"nombre": "Ana", "rol": "admin"}  # Atributos del usuario
coordenadas = (12, 8)  # Tupla fija
resumen = perfil["nombre"] + " en " + str(coordenadas)  # Resumen
print(usuarios_unicos)  # Mostramos únicos
print(perfil)  # Mostramos el perfil
print(resumen)  # Mostramos el resumen
print(len(usuarios_unicos))  # Contamos únicos
#
# Verás esto
# Verás un set de usuarios únicos, el perfil y el resumen.
#
# Por qué funciona
# Cada estructura cumple un rol: únicos, atributos y pares fijos.
#
# Lo típico que sale mal
# - Usar lista cuando necesitas claves.
# - Usar set cuando necesitas orden.
""",
            ),
            (
                "Comprensión de listas",
                """# Aprende esto
# Aprenderás a crear listas nuevas con comprensiones.
# Verás cómo transformar datos sin modificar el original.
# Mantendrás el código compacto y claro.
#
# Haz esto
precios = [10, 20, 30]  # Lista base
precios_con_iva = [p * 1.18 for p in precios]  # Nueva lista
copia_precios = precios.copy()  # Copia independiente
copia_precios.append(40)  # Modificamos solo la copia
print(precios)  # Mostramos original
print(precios_con_iva)  # Mostramos con IVA
print(copia_precios)  # Mostramos copia
print(len(precios_con_iva))  # Contamos elementos
#
# Verás esto
# Verás la lista original intacta y la lista con IVA.
#
# Por qué funciona
# La comprensión crea una lista nueva y copy evita alias.
#
# Lo típico que sale mal
# - Modificar la lista original por accidente.
# - Olvidar que copy es superficial.
""",
            ),
            (
                "Diccionario por comprensión",
                """# Aprende esto
# Aprenderás a crear diccionarios con comprensiones.
# Verás cómo mapear claves a valores calculados.
# Practicarás estructuras útiles para búsquedas.
#
# Haz esto
precios = [10, 20, 30]  # Lista base
indice = {p: p * 1.18 for p in precios}  # Diccionario con IVA
precio_20 = indice.get(20, 0)  # Buscamos una clave
mensaje = "Precio 20 con IVA: " + str(precio_20)  # Mensaje
print(indice)  # Mostramos el diccionario
print(mensaje)  # Mostramos el mensaje
print(len(indice))  # Contamos claves
print(20 in indice)  # Verificamos pertenencia
#
# Verás esto
# Verás un diccionario con precios calculados y True en la búsqueda.
#
# Por qué funciona
# La comprensión define claves y valores en una sola expresión.
#
# Lo típico que sale mal
# - Repetir claves y sobrescribir valores.
# - Olvidar que las claves deben ser únicas.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una lista con tres números y muestra el primero y el último.",
                "hints": ["Usa índices 0 y -1"],
                "solution": "numeros = [1, 2, 3]\nprint(numeros[0])\nprint(numeros[-1])",
            },
            {
                "question": "Crea una tupla con dos valores y desempaquétalos en variables.",
                "hints": ["Usa x, y = tupla"],
                "solution": "punto = (4, 5)\nx, y = punto\nprint(x, y)",
            },
            {
                "question": "Crea un diccionario con claves 'nombre' y 'edad'. Muestra el nombre.",
                "hints": ["Usa dict['nombre']"],
                "solution": "persona = {'nombre': 'Ana', 'edad': 30}\nprint(persona['nombre'])",
            },
            {
                "question": "Elimina duplicados de una lista usando un set.",
                "hints": ["Convierte con set()"],
                "solution": "valores = [1, 1, 2, 3]\nunicos = set(valores)\nprint(unicos)",
            },
            {
                "question": "Crea una lista de diccionarios con dos productos y muestra el total de precios.",
                "hints": ["Usa índices y claves"],
                "solution": "productos = [{'precio': 10}, {'precio': 20}]\ntotal = productos[0]['precio'] + productos[1]['precio']\nprint(total)",
            },
            {
                "question": "Crea una comprensión que eleve al cuadrado una lista de números.",
                "hints": ["Usa [x * x for x in lista]"],
                "solution": "numeros = [2, 3, 4]\ncuadrados = [n * n for n in numeros]\nprint(cuadrados)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget

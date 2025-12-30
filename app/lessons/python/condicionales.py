from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class CondicionalesLesson(Lesson):
    TITLE = "Condicionales"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["if", "elif", "else", "comparaciones"]

    def summary(self) -> str:
        return (
            "Aprende desde cero cómo tomar decisiones con if, elif y else, "
            "usando comparaciones claras y evitando errores comunes."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: decidir es el corazón de un programa
Un programa útil toma decisiones: mostrar un mensaje si hay stock, validar una edad, aplicar un descuento o detener una
acción. En Python, esas decisiones se expresan con `if`, `elif` y `else`. La clave es escribir condiciones claras y
predecibles. En esta lección aprenderás a construir condicionales paso a paso, con ejemplos contextualizados y errores
comunes explicados.

## Paso 1: Condición simple con if
El condicional más simple evalúa una condición y ejecuta un bloque si es verdadera.

**Aprende esto**
- Aprenderás a usar `if` con una comparación básica.
- Verás cómo construir un mensaje según el resultado.

**Haz esto**
print("ok")  # Confirmamos
```
stock = 5  # Unidades disponibles
umbral = 3  # Mínimo requerido
hay_stock = stock > umbral  # Evaluamos la condición
mensaje = "Stock suficiente"  # Mensaje base
if hay_stock:  # Si hay stock, mostramos el mensaje
    print(mensaje)  # Mostramos el mensaje
print(hay_stock)  # Mostramos el booleano
print(stock)  # Mostramos el stock
print("ok")  # Confirmamos
```

**Verás esto**
Verás el mensaje de stock suficiente y el booleano `True`.

**Por qué funciona**
La comparación `stock > umbral` devuelve `True`. El bloque `if` se ejecuta solo cuando la condición es verdadera.

**Lo típico que sale mal**
- Usar `=` en lugar de `==` dentro de una condición.
- Confundir el orden de la comparación.

## Paso 2: if/else para dos caminos
Cuando hay dos posibilidades claras, `else` ayuda a cubrir el caso contrario.

**Aprende esto**
- Aprenderás a usar `else` para cubrir el caso negativo.
- Verás cómo evitar mensajes ambiguos.

**Haz esto**
print("ok")  # Confirmamos
```
edad = 17  # Edad del usuario
mayor_edad = edad >= 18  # Evaluamos si es mayor
if mayor_edad:  # Si es mayor
    mensaje = "Acceso permitido"  # Mensaje positivo
else:  # Si no es mayor
    mensaje = "Acceso restringido"  # Mensaje negativo
print(mensaje)  # Mostramos el resultado
print(mayor_edad)  # Mostramos el booleano
print("ok")  # Confirmamos
```

**Verás esto**
Verás `Acceso restringido` y `False`.

**Por qué funciona**
`>=` evalúa si la edad alcanza el mínimo. El `else` cubre el caso opuesto sin necesidad de otra condición.

**Lo típico que sale mal**
- Olvidar el `else` y no cubrir el caso negativo.
- Invertir la comparación y mostrar el mensaje incorrecto.

## Paso 3: elif para múltiples condiciones
`elif` permite evaluar múltiples condiciones de forma ordenada.

**Aprende esto**
- Aprenderás a encadenar condiciones con `elif`.
- Verás por qué el orden de evaluación importa.

**Haz esto**
print("ok")  # Confirmamos
```
puntaje = 82  # Puntaje obtenido
if puntaje >= 90:  # Primer rango
    nivel = "Excelente"  # Nivel alto
elif puntaje >= 70:  # Segundo rango
    nivel = "Aprobado"  # Nivel medio
else:  # Resto de casos
    nivel = "Reforzar"  # Nivel bajo
print(nivel)  # Mostramos el nivel
print(puntaje)  # Mostramos el puntaje
print("ok")  # Confirmamos
```

**Verás esto**
Verás `Aprobado` y el puntaje `82`.

**Por qué funciona**
Python evalúa de arriba hacia abajo y usa el primer bloque verdadero. Por eso el orden de las condiciones es clave.

**Lo típico que sale mal**
- Poner primero la condición más general y bloquear las siguientes.
- Olvidar el `else` y dejar casos sin cubrir.

## Paso 4: Operadores lógicos (and/or)
Combinar condiciones te permite decisiones más específicas.

**Aprende esto**
- Aprenderás a combinar condiciones con `and` y `or`.
- Verás cómo construir reglas más reales.

**Haz esto**
print("ok")  # Confirmamos
```
precio = 120  # Precio del producto
es_cliente = True  # Indica si es cliente
aplica_descuento = precio > 100 and es_cliente  # Reglas combinadas
if aplica_descuento:  # Si aplica descuento
    mensaje = "Descuento aplicado"  # Mensaje
else:  # Si no aplica
    mensaje = "Sin descuento"  # Mensaje
print(mensaje)  # Mostramos el mensaje
print(aplica_descuento)  # Mostramos el booleano
print("ok")  # Confirmamos
```

**Verás esto**
Verás `Descuento aplicado` y `True`.

**Por qué funciona**
`and` exige que ambas condiciones sean verdaderas. Como el precio es alto y es cliente, la condición se cumple.

**Lo típico que sale mal**
- Usar `and` cuando necesitas `or`.
- No agrupar condiciones y obtener resultados inesperados.

## Paso 5: Pertenencia e identidad
A veces necesitas saber si un valor está dentro de una colección o si algo es `None`.

**Aprende esto**
- Aprenderás a usar `in` para pertenencia.
- Verás cómo comparar con `is` cuando hay `None`.

**Haz esto**
print("ok")  # Confirmamos
```
roles = ["admin", "editor"]  # Roles permitidos
rol = "editor"  # Rol actual
es_valido = rol in roles  # Verificamos pertenencia
resultado = None  # Aún no hay resultado
if es_valido:  # Si el rol es válido
    resultado = "Acceso"  # Asignamos resultado
print(es_valido)  # Mostramos el booleano
print(resultado is None)  # Verificamos si sigue vacío
print(resultado)  # Mostramos el resultado
print("ok")  # Confirmamos
```

**Verás esto**
Verás `True`, `False` y el texto `Acceso`.

**Por qué funciona**
`in` revisa pertenencia en la lista y `is` compara identidad con `None`, que es un valor especial único.

**Lo típico que sale mal**
- Usar `== None` en lugar de `is None`.
- Buscar pertenencia en una lista sin normalizar texto.

## Paso 6: Condiciones con valores "truthy"
Python considera ciertos valores como verdaderos o falsos sin comparaciones explícitas.

**Aprende esto**
- Aprenderás qué significa truthy y falsy.
- Verás cómo usarlo con cuidado en condicionales.

**Haz esto**
print("ok")  # Confirmamos
```
lista = []  # Lista vacía
mensaje = "Lista vacía"  # Mensaje base
if lista:  # La lista vacía es falsy
    mensaje = "Lista con datos"  # Mensaje alterno
print(mensaje)  # Mostramos el mensaje
lista.append("dato")  # Agregamos un dato
if lista:  # Ahora la lista es truthy
    print("Lista con datos")  # Mostramos el mensaje
print(len(lista))  # Mostramos la cantidad
print("ok")  # Confirmamos
```

**Verás esto**
Verás `Lista vacía`, luego `Lista con datos` y el número 1.

**Por qué funciona**
Las colecciones vacías son falsy y las no vacías son truthy. Esto simplifica ciertas validaciones.

**Lo típico que sale mal**
- Usar truthy sin entender qué valores cuentan como falsy.
- Confundir una lista vacía con `None`.

## Más allá (nivel pro): condiciones legibles y validación
En proyectos reales conviene escribir condiciones claras y pequeñas funciones para validar datos.

**Aprende esto**
- Aprenderás a combinar condiciones con nombres legibles.
- Verás cómo evitar condicionales gigantes usando variables intermedias.

**Haz esto**
print("ok")  # Confirmamos
```
edad = 20  # Edad del usuario
acepta_terminos = True  # Indicador de aceptación
es_mayor = edad >= 18  # Condición 1
puede_ingresar = es_mayor and acepta_terminos  # Condición final
mensaje = "Acceso" if puede_ingresar else "Bloqueado"  # Mensaje final
print(puede_ingresar)  # Mostramos el booleano
print(mensaje)  # Mostramos el mensaje
print("ok")  # Confirmamos
```

**Verás esto**
Verás `True` y `Acceso`.

**Por qué funciona**
Separar condiciones en variables con nombre hace el código más legible y reduce errores al combinar lógica.

**Lo típico que sale mal**
- Escribir condiciones largas sin nombres y perder claridad.
- Repetir la misma condición en varios lugares.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Usar = en lugar de ==",
                "El operador = asigna, no compara; causa errores de sintaxis.",
            ),
            (
                "Orden incorrecto en elif",
                "Una condición general primero puede ocultar casos específicos.",
            ),
            (
                "Olvidar else",
                "Dejar casos sin cubrir crea resultados silenciosos.",
            ),
            (
                "Comparar con None usando ==",
                "La comparación correcta es `is None`.",
            ),
            (
                "No normalizar texto",
                "Comparar strings sin lower() produce resultados inconsistentes.",
            ),
            (
                "Confundir and/or",
                "and requiere ambas condiciones; or solo una.",
            ),
            (
                "No agrupar condiciones",
                "Falta de paréntesis puede cambiar la lógica.",
            ),
            (
                "Usar truthy sin claridad",
                "No todos saben que una lista vacía es falsy.",
            ),
            (
                "Comparar floats directamente",
                "Comparaciones exactas pueden fallar por precisión.",
            ),
            (
                "No validar rangos",
                "Olvidar rangos causa decisiones incorrectas.",
            ),
            (
                "Confundir identidad con igualdad",
                "is compara identidad, no valores.",
            ),
            (
                "Repetir condiciones",
                "Duplicar lógica aumenta el riesgo de inconsistencias.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "if simple",
                """# Aprende esto
# Aprenderás a usar un if básico.
# Verás cómo una condición controla un bloque.
# Practicarás con un caso de stock.
#
# Haz esto
stock = 5  # Unidades disponibles
umbral = 3  # Mínimo requerido
hay_stock = stock > umbral  # Evaluamos condición
mensaje = "Stock suficiente"  # Mensaje base
if hay_stock:  # Si hay stock
    print(mensaje)  # Mostramos el mensaje
print(hay_stock)  # Mostramos el booleano
print(stock)  # Mostramos el stock
#
# Verás esto
# Verás el mensaje y True.
#
# Por qué funciona
# La condición se evalúa y el bloque se ejecuta si es verdadera.
#
# Lo típico que sale mal
# - Usar = en lugar de ==.
# - Confundir el orden de la comparación.
""",
            ),
            (
                "if/else",
                """# Aprende esto
# Aprenderás a cubrir dos caminos con else.
# Verás mensajes claros en cada caso.
# Evitarás resultados ambiguos.
#
# Haz esto
edad = 17  # Edad
mayor_edad = edad >= 18  # Evaluamos condición
if mayor_edad:  # Si es mayor
    mensaje = "Acceso permitido"  # Mensaje positivo
else:  # Si no es mayor
    mensaje = "Acceso restringido"  # Mensaje negativo
print(mensaje)  # Mostramos el mensaje
print(mayor_edad)  # Mostramos el booleano
#
# Verás esto
# Verás "Acceso restringido" y False.
#
# Por qué funciona
# else cubre el caso en que la condición es falsa.
#
# Lo típico que sale mal
# - Olvidar el else.
# - Invertir la comparación.
""",
            ),
            (
                "elif para rangos",
                """# Aprende esto
# Aprenderás a usar elif con rangos.
# Verás cómo el orden afecta el resultado.
# Practicarás con niveles de puntaje.
#
# Haz esto
puntaje = 82  # Puntaje
if puntaje >= 90:  # Alto
    nivel = "Excelente"  # Nivel alto
elif puntaje >= 70:  # Medio
    nivel = "Aprobado"  # Nivel medio
else:  # Bajo
    nivel = "Reforzar"  # Nivel bajo
print(nivel)  # Mostramos el nivel
print(puntaje)  # Mostramos el puntaje
#
# Verás esto
# Verás "Aprobado" y 82.
#
# Por qué funciona
# Python evalúa en orden y toma el primer bloque verdadero.
#
# Lo típico que sale mal
# - Poner primero la condición más general.
# - Dejar casos sin cubrir.
""",
            ),
            (
                "Operadores lógicos",
                """# Aprende esto
# Aprenderás a combinar condiciones con and.
# Verás cómo construir reglas reales.
# Confirmarás el resultado con un booleano.
#
# Haz esto
precio = 120  # Precio del producto
es_cliente = True  # Indicador de cliente
aplica_descuento = precio > 100 and es_cliente  # Regla combinada
if aplica_descuento:  # Si aplica descuento
    mensaje = "Descuento aplicado"  # Mensaje
else:  # Caso contrario
    mensaje = "Sin descuento"  # Mensaje
print(mensaje)  # Mostramos mensaje
print(aplica_descuento)  # Mostramos booleano
#
# Verás esto
# Verás "Descuento aplicado" y True.
#
# Por qué funciona
# and requiere que ambas condiciones sean verdaderas.
#
# Lo típico que sale mal
# - Usar and cuando corresponde or.
# - No agrupar condiciones.
""",
            ),
            (
                "Pertenencia con in",
                """# Aprende esto
# Aprenderás a verificar pertenencia en listas.
# Verás cómo usar in de forma clara.
# Crearás un mensaje basado en la validación.
#
# Haz esto
roles = ["admin", "editor"]  # Roles permitidos
rol = "editor"  # Rol actual
es_valido = rol in roles  # Verificamos pertenencia
mensaje = "Rol válido" if es_valido else "Rol inválido"  # Mensaje
rol_mayus = rol.upper()  # Normalizamos para mostrar
print(es_valido)  # Mostramos booleano
print(mensaje)  # Mostramos mensaje
print(len(roles))  # Mostramos cantidad
print(rol_mayus)  # Mostramos el rol en mayúsculas
#
# Verás esto
# Verás True y "Rol válido".
#
# Por qué funciona
# in revisa si el valor está en la colección.
#
# Lo típico que sale mal
# - No normalizar texto antes de comparar.
# - Confundir in con igualdad.
""",
            ),
            (
                "Comparar con None",
                """# Aprende esto
# Aprenderás a usar is con None.
# Verás cómo actualizar un resultado.
# Evitarás comparar con ==.
#
# Haz esto
resultado = None  # Aún no hay resultado
valor = 5  # Valor base
resultado = valor * 2  # Calculamos resultado
es_nulo = resultado is None  # Verificamos si es None
mensaje = "Sin resultado" if es_nulo else "Con resultado"  # Mensaje
print(es_nulo)  # Mostramos booleano
print(resultado)  # Mostramos resultado
print(resultado is not None)  # Confirmamos que existe
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás False, 10 y True.
#
# Por qué funciona
# None es un singleton y se compara con is.
#
# Lo típico que sale mal
# - Usar == None.
# - Confundir None con 0.
""",
            ),
            (
                "Truthy y falsy",
                """# Aprende esto
# Aprenderás a usar truthy con listas.
# Verás cómo una lista vacía es falsy.
# Confirmarás con len.
#
# Haz esto
lista = []  # Lista vacía
mensaje = "Lista vacía"  # Mensaje base
if lista:  # Lista vacía es falsy
    mensaje = "Lista con datos"  # Mensaje alterno
print(mensaje)  # Mostramos mensaje
lista.append("dato")  # Agregamos un dato
if lista:  # Ahora es truthy
    print("Lista con datos")  # Mostramos mensaje
print(len(lista))  # Cantidad
#
# Verás esto
# Verás "Lista vacía", luego "Lista con datos" y 1.
#
# Por qué funciona
# Colecciones vacías son falsy; no vacías son truthy.
#
# Lo típico que sale mal
# - Confundir lista vacía con None.
# - Usar truthy sin claridad.
""",
            ),
            (
                "Condición con variable intermedia",
                """# Aprende esto
# Aprenderás a usar variables para claridad.
# Verás cómo una condición se vuelve más legible.
# Evitarás condicionales gigantes.
#
# Haz esto
edad = 20  # Edad
acepta_terminos = True  # Acepta términos
es_mayor = edad >= 18  # Condición de edad
puede_ingresar = es_mayor and acepta_terminos  # Condición final
mensaje = "Acceso" if puede_ingresar else "Bloqueado"  # Mensaje
print(puede_ingresar)  # Mostramos booleano
print(mensaje)  # Mostramos mensaje
print(es_mayor)  # Mostramos condición base
#
# Verás esto
# Verás True, "Acceso" y True.
#
# Por qué funciona
# Separar condiciones mejora la lectura y reduce errores.
#
# Lo típico que sale mal
# - Repetir la misma condición varias veces.
# - Usar nombres poco claros en variables lógicas.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea un if que muestre 'Mayor' si edad >= 18.",
                "hints": ["Usa >="],
                "solution": "edad = 20\nif edad >= 18:\n    print('Mayor')",
            },
            {
                "question": "Usa if/else para mostrar 'Aprobado' o 'Reprobado' según nota >= 60.",
                "hints": ["Usa else"],
                "solution": "nota = 55\nif nota >= 60:\n    print('Aprobado')\nelse:\n    print('Reprobado')",
            },
            {
                "question": "Crea un if/elif/else para rangos de temperatura.",
                "hints": ["Usa tres rangos"],
                "solution": "temp = 18\nif temp >= 30:\n    print('Calor')\nelif temp >= 20:\n    print('Templado')\nelse:\n    print('Frío')",
            },
            {
                "question": "Combina dos condiciones con and.",
                "hints": ["Usa and"],
                "solution": "precio = 120\nes_cliente = True\nif precio > 100 and es_cliente:\n    print('Descuento')",
            },
            {
                "question": "Verifica si 'admin' está en una lista de roles.",
                "hints": ["Usa in"],
                "solution": "roles = ['admin', 'editor']\nprint('admin' in roles)",
            },
            {
                "question": "Comprueba si una variable es None usando is.",
                "hints": ["Usa is None"],
                "solution": "resultado = None\nif resultado is None:\n    print('Sin resultado')",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget

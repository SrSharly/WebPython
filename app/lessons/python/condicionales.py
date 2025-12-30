from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class CondicionalesLesson(Lesson):
    TITLE = "Condicionales"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["if", "elif", "else", "booleanos"]

    def summary(self) -> str:
        return (
            "Aprende a tomar decisiones con if/elif/else, comparaciones claras y lógica booleana sin confusiones."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: decidir es programar
La mayoría de los programas existen para decidir algo: si un usuario tiene acceso, si un pago es válido, si se debe mostrar
un mensaje u otro. Los condicionales son la herramienta para expresar esas decisiones. Aprender a escribir condiciones claras
te ahorra errores y evita comportamientos inesperados.

En esta lección aprenderás desde cero cómo usar `if`, `elif` y `else`, cómo comparar valores, cómo combinar condiciones y
cómo interpretar booleanos. También verás la importancia de la indentación, porque en Python el bloque se define por el
espaciado. Al final tendrás un conjunto de patrones para tomar decisiones con seguridad.

### Nota (CalloutBox: note)
Los condicionales se leen como preguntas. Si la pregunta está mal formulada, la respuesta del programa también lo estará.

## Paso 1: la estructura básica if/else
El `if` ejecuta un bloque si la condición es verdadera. El `else` se usa cuando la condición no se cumple. Esta estructura
básica cubre decisiones binarias: sí/no, válido/no válido, permitido/bloqueado.

Es importante que la condición sea una expresión booleana. Puedes usar comparaciones como `==`, `!=`, `>`, `<` o comprobar
si una variable ya es `True` o `False`.

## Paso 2: múltiples caminos con elif
Cuando hay más de dos posibilidades, `elif` te permite agregar caminos intermedios. El flujo se evalúa de arriba hacia abajo
y solo el primer bloque verdadero se ejecuta. Esto hace que el orden sea importante.

Aprenderás a ordenar condiciones de lo más específico a lo más general para que el resultado sea predecible.

## Paso 3: comparaciones claras
Comparar números es directo, pero comparar texto requiere cuidado con mayúsculas, espacios y formatos. También aprenderás a
comparar con `None` usando `is None` para evitar errores de identidad.

Es una buena práctica asignar nombres descriptivos a las condiciones. Si el nombre explica la lógica, el `if` se vuelve
legible como una frase.

### Buenas prácticas (CalloutBox: best_practice)
Si una condición es larga, guárdala en una variable con nombre claro. Eso hace que el `if` sea fácil de leer y depurar.

## Paso 4: lógica booleana (and, or, not)
Las palabras clave `and`, `or` y `not` permiten combinar condiciones. `and` exige que ambas sean verdaderas; `or` basta con
una; `not` invierte el resultado. Con esta lógica puedes representar reglas reales: “si hay saldo y el usuario está activo”.

## Paso 5: valores verdaderos y falsos
En Python, algunos valores se consideran falsos: `0`, `""`, `[]`, `None`. Aprender este detalle te ayuda a escribir
condiciones más naturales: `if lista:` en lugar de `if len(lista) > 0`. Aun así, hay momentos donde la comparación explícita
es más clara. La regla es: claridad antes que atajos.

## Paso 6: orden y legibilidad
Si el orden de las condiciones no es correcto, puedes tener bugs silenciosos. Por ejemplo, si evalúas “mayor de edad” antes
que “menor de 12”, el caso de 10 años nunca se ejecutará. Ordena de más específico a más general.

### Advertencia (CalloutBox: warning)
Evita condiciones imposibles o redundantes. Si una condición siempre es verdadera, tu `else` nunca se ejecutará.

## Más allá (nivel pro)
En proyectos reales, los condicionales definen reglas de negocio. Una pequeña ambigüedad puede convertirse en un error
costoso. Por eso, invertir tiempo en claridad es una decisión pro.

### Consejos pro
- Nombra condiciones complejas: `es_mayor = edad >= 18` mejora lectura y pruebas.
- Agrupa reglas con paréntesis para evitar confusiones en `and` y `or`.
- Prefiere comparaciones explícitas cuando un valor puede ser `0` o `""`.
- Ordena `elif` de más específico a más general y documenta la intención.
- Si la lógica crece, considera moverla a una función con nombre descriptivo.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Olvidar los dos puntos",
                "Cada `if`, `elif` y `else` termina con `:`. Sin eso, Python marca error de sintaxis.",
            ),
            (
                "Indentación incorrecta",
                "Si el bloque no está indentado, Python no sabe qué pertenece al `if`.",
            ),
            (
                "Usar = en lugar de ==",
                "`=` asigna, `==` compara. Mezclarlos cambia el significado de la condición.",
            ),
            (
                "Comparar con None usando ==",
                "Para `None` se recomienda `is None` para comparar identidad.",
            ),
            (
                "Condiciones demasiado largas",
                "Cuando una condición ocupa varias líneas sin nombre, se vuelve difícil de entender y depurar.",
            ),
            (
                "Orden incorrecto en elif",
                "Si pones un caso general primero, los casos específicos nunca se ejecutan.",
            ),
            (
                "Confiar en valores falsy sin intención",
                "`0` y `""` son falsos. Si esos valores son válidos, debes comparar explícitamente.",
            ),
            (
                "No cubrir todos los casos",
                "Si no hay `else` y ninguna condición se cumple, puede faltar un comportamiento esperado.",
            ),
            (
                "Confundir and/or",
                "`and` exige ambas condiciones; `or` basta con una. Usarlos mal cambia la lógica.",
            ),
            (
                "Usar not sin paréntesis",
                "`not` cambia la prioridad. Si la expresión es larga, usa paréntesis para claridad.",
            ),
            (
                "Comparar strings con espacios",
                "Un espacio extra cambia el resultado. Usa `strip()` si el texto viene de entrada.",
            ),
            (
                "No imprimir para depurar",
                "Cuando un `if` no entra, imprime valores y tipos para confirmar la condición.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "If básico",
                """# Aprende esto
# Aprenderás a usar if con una condición simple.
# Verás cómo entra o no en el bloque.
# Entenderás la importancia de la indentación.
#
# Haz esto
edad = 20  # Guardamos la edad
if edad >= 18:  # Comprobamos mayoría de edad
    print("Acceso permitido")  # Mostramos mensaje
else:  # Caso contrario
    print("Acceso denegado")  # Mostramos mensaje
#
# Verás esto
# Verás "Acceso permitido".
#
# Por qué funciona
# La condición es verdadera y ejecuta el bloque if.
#
# Lo típico que sale mal
# - Olvidar los dos puntos.
# - No indentar el bloque.
""",
            ),
            (
                "If con comparación de texto",
                """# Aprende esto
# Aprenderás a comparar texto con ==.
# Verás cómo afecta mayúsculas y espacios.
# Entenderás la necesidad de normalizar.
#
# Haz esto
estado = "activo"  # Estado actual
if estado == "activo":  # Comparamos texto
    print("Usuario activo")  # Mostramos mensaje
else:  # Caso contrario
    print("Usuario inactivo")  # Mostramos mensaje
#
# Verás esto
# Verás "Usuario activo".
#
# Por qué funciona
# == compara el contenido exacto del string.
#
# Lo típico que sale mal
# - Comparar sin normalizar mayúsculas.
# - Incluir espacios invisibles.
""",
            ),
            (
                "Elif para varias opciones",
                """# Aprende esto
# Aprenderás a usar elif con varios casos.
# Verás cómo se evalúan en orden.
# Entenderás el flujo de arriba hacia abajo.
#
# Haz esto
nota = 7  # Nota del estudiante
if nota >= 9:  # Caso excelente
    resultado = "Excelente"  # Guardamos resultado
elif nota >= 7:  # Caso aprobado
    resultado = "Aprobado"  # Guardamos resultado
else:  # Caso desaprobado
    resultado = "Reprobado"  # Guardamos resultado
print(resultado)  # Mostramos resultado
#
# Verás esto
# Verás "Aprobado".
#
# Por qué funciona
# El primer elif verdadero detiene la evaluación.
#
# Lo típico que sale mal
# - Ordenar mal los rangos.
# - Olvidar el else final.
""",
            ),
            (
                "Combinar condiciones con and",
                """# Aprende esto
# Aprenderás a usar and para dos condiciones.
# Verás que ambas deben ser True.
# Entenderás cómo validar reglas múltiples.
#
# Haz esto
saldo = 50  # Saldo disponible
activo = True  # Estado del usuario
if saldo >= 20 and activo:  # Ambas condiciones
    print("Compra permitida")  # Mostramos mensaje
else:  # Caso contrario
    print("Compra denegada")  # Mostramos mensaje
#
# Verás esto
# Verás "Compra permitida".
#
# Por qué funciona
# and exige que saldo y activo sean verdaderos.
#
# Lo típico que sale mal
# - Usar and cuando era or.
# - Olvidar convertir a booleanos.
""",
            ),
            (
                "Condiciones con or",
                """# Aprende esto
# Aprenderás a usar or para alternativas.
# Verás que basta una condición verdadera.
# Entenderás la lógica de permisos.
#
# Haz esto
es_admin = False  # Rol admin
es_editor = True  # Rol editor
if es_admin or es_editor:  # Al menos uno
    print("Acceso a edición")  # Mostramos mensaje
else:  # Caso contrario
    print("Sin permisos")  # Mostramos mensaje
#
# Verás esto
# Verás "Acceso a edición".
#
# Por qué funciona
# or evalúa verdadero si alguna condición lo es.
#
# Lo típico que sale mal
# - Usar or cuando se necesitaban ambas condiciones.
# - No agrupar condiciones complejas.
""",
            ),
            (
                "Usar not",
                """# Aprende esto
# Aprenderás a invertir una condición con not.
# Verás cómo leerlo como negación.
# Entenderás cuándo ayuda a la claridad.
#
# Haz esto
mantenimiento = False  # Estado del sistema
if not mantenimiento:  # Negamos el estado
    print("Sistema disponible")  # Mostramos mensaje
else:  # Caso contrario
    print("Sistema en mantenimiento")  # Mostramos mensaje
#
# Verás esto
# Verás "Sistema disponible".
#
# Por qué funciona
# not invierte el booleano.
#
# Lo típico que sale mal
# - Usar not sin paréntesis en expresiones largas.
# - Leer la condición al revés.
""",
            ),
            (
                "Comparar con None",
                """# Aprende esto
# Aprenderás a comprobar ausencia con None.
# Verás el uso correcto de is None.
# Entenderás por qué es identidad.
#
# Haz esto
resultado = None  # Aún no calculado
if resultado is None:  # Comprobamos ausencia
    resultado = 10  # Asignamos un valor
print(resultado)  # Mostramos resultado
#
# Verás esto
# Verás 10.
#
# Por qué funciona
# is None verifica identidad de ausencia.
#
# Lo típico que sale mal
# - Usar == con None sin necesidad.
# - Confundir None con 0.
""",
            ),
            (
                "Condiciones con listas",
                """# Aprende esto
# Aprenderás a usar listas en condiciones.
# Verás valores falsy y truthy.
# Entenderás cuándo es más claro usar len().
#
# Haz esto
pendientes = ["tarea1", "tarea2"]  # Lista de tareas
if pendientes:  # Lista no vacía
    print("Hay tareas")  # Mostramos mensaje
else:  # Lista vacía
    print("No hay tareas")  # Mostramos mensaje
#
# Verás esto
# Verás "Hay tareas".
#
# Por qué funciona
# Una lista no vacía es True.
#
# Lo típico que sale mal
# - Usar esta forma cuando 0 es un valor válido.
# - Confundir lista vacía con None.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Escribe un if que muestre 'Mayor de edad' si edad >= 18, si no 'Menor de edad'.",
                "hints": ["Usa if/else.", "No olvides los dos puntos."],
                "solution": """edad = 16
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")""",
            },
            {
                "question": "Usa elif para clasificar una nota: >= 9 Excelente, >= 7 Aprobado, si no Reprobado.",
                "hints": ["Ordena de mayor a menor.", "Usa elif."],
                "solution": """nota = 8
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprobado")
else:
    print("Reprobado")""",
            },
            {
                "question": "Crea una condición con and que valide saldo >= 50 y usuario activo.",
                "hints": ["Define saldo y activo.", "Usa and."],
                "solution": """saldo = 60
activo = True
if saldo >= 50 and activo:
    print("Pago permitido")""",
            },
            {
                "question": "Crea una condición con or para permitir acceso si es_admin o es_editor.",
                "hints": ["Usa or.", "Imprime un mensaje."],
                "solution": """es_admin = False
es_editor = True
if es_admin or es_editor:
    print("Acceso permitido")""",
            },
            {
                "question": "Usa not para mostrar un mensaje si no hay mantenimiento.",
                "hints": ["Define mantenimiento = False.", "Usa not en el if."],
                "solution": """mantenimiento = False
if not mantenimiento:
    print("Disponible")""",
            },
            {
                "question": "Comprueba si una lista está vacía y muestra un mensaje.",
                "hints": ["Usa if lista.", "Una lista vacía es False."],
                "solution": """items = []
if items:
    print("Hay items")
else:
    print("Lista vacía")""",
            },
        ]

from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class CondicionalesLesson(Lesson):
    TITLE = "Condicionales"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["if", "else", "elif", "comparaciones"]

    def summary(self) -> str:
        return (
            "Aprende a tomar decisiones con if/elif/else, a comparar valores y a escribir "
            "condiciones claras que eviten errores comunes."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: tomar decisiones es programar
Los condicionales permiten ejecutar código solo cuando se cumple una condición. Con ellos controlas flujos:
validar datos, decidir descuentos o elegir rutas de ejecución.

## Paso 1: if básico
El bloque `if` se ejecuta solo si la condición es verdadera.

**Aprende esto**
- Aprenderás a evaluar una condición simple.
- Verás cómo ejecutar un bloque cuando se cumple.

**Haz esto**
```
edad = 20  # Edad del usuario
es_mayor = edad >= 18  # Comparamos con 18
if es_mayor:  # Si es verdadero
    mensaje = "Puede ingresar"  # Definimos el mensaje
else:  # En caso contrario
    mensaje = "No puede ingresar"  # Mensaje alternativo
print(mensaje)  # Mostramos el resultado
```

**Verás esto**
Verás `Puede ingresar`.

**Por qué funciona**
`edad >= 18` devuelve True y el bloque `if` se ejecuta.

**Lo típico que sale mal**
- Usar `=` en lugar de `==` en comparaciones.
- Olvidar el `else` cuando necesitas cubrir ambos casos.

## Paso 2: elif para múltiples caminos
`elif` permite evaluar varias condiciones sin usar múltiples `if` separados.

**Aprende esto**
- Aprenderás a encadenar condiciones con `elif`.
- Verás cómo elegir un único camino.

**Haz esto**
```
puntaje = 75  # Puntaje del examen
if puntaje >= 90:  # Primera condición
    nivel = "Excelente"  # Nivel alto
elif puntaje >= 70:  # Segunda condición
    nivel = "Aprobado"  # Nivel medio
else:  # Si no cumple ninguna
    nivel = "Reprobado"  # Nivel bajo
print(nivel)  # Mostramos el nivel
```

**Verás esto**
Verás `Aprobado`.

**Por qué funciona**
Python evalúa de arriba hacia abajo y se queda con la primera condición verdadera.

**Lo típico que sale mal**
- Colocar condiciones más generales primero y bloquear las específicas.
- Repetir `if` separados y obtener múltiples resultados.

## Paso 3: Comparaciones y operadores lógicos
Puedes combinar condiciones con `and`, `or` y `not`.

**Aprende esto**
- Aprenderás a combinar comparaciones en una sola condición.
- Verás cómo controlar dos requisitos a la vez.

**Haz esto**
```
edad = 22  # Edad del usuario
saldo = 50  # Saldo disponible
es_adulto = edad >= 18  # Condición 1
saldo_suficiente = saldo >= 30  # Condición 2
if es_adulto and saldo_suficiente:  # Ambas condiciones
    estado = "Compra permitida"  # Mensaje positivo
else:  # Si alguna falla
    estado = "Compra rechazada"  # Mensaje negativo
print(estado)  # Mostramos el estado
```

**Verás esto**
Verás `Compra permitida`.

**Por qué funciona**
`and` exige que ambas condiciones sean True. Si alguna es False, se ejecuta el else.

**Lo típico que sale mal**
- Usar `or` cuando necesitas que todas se cumplan.
- No separar condiciones en variables y perder claridad.

## Paso 4: Comparar cadenas de texto
Comparar strings es común en menús y validaciones.

**Aprende esto**
- Aprenderás a comparar texto con seguridad.
- Verás cómo normalizar para evitar errores por mayúsculas.

**Haz esto**
```
entrada = "  Si "  # Texto del usuario
respuesta = entrada.strip().lower()  # Normalizamos
if respuesta == "si":  # Comparamos con texto esperado
    mensaje = "Confirmado"  # Resultado positivo
else:  # Si no coincide
    mensaje = "Cancelado"  # Resultado negativo
print(mensaje)  # Mostramos el mensaje
```

**Verás esto**
Verás `Confirmado`.

**Por qué funciona**
`strip` elimina espacios y `lower` unifica el texto para compararlo con seguridad.

**Lo típico que sale mal**
- Comparar texto sin limpiar espacios.
- Olvidar normalizar mayúsculas.

## Paso 5: Condiciones con rangos
A veces necesitas verificar si algo está entre dos valores.

**Aprende esto**
- Aprenderás a usar comparaciones encadenadas.
- Verás cómo validar rangos de forma legible.

**Haz esto**
```
temperatura = 23  # Temperatura actual
if 20 <= temperatura <= 25:  # Comprobamos rango
    estado = "Confort"  # Estado adecuado
else:  # Fuera del rango
    estado = "Ajustar"  # Mensaje de ajuste
print(estado)  # Mostramos el estado
```

**Verás esto**
Verás `Confort`.

**Por qué funciona**
Python permite comparar un valor dentro de un rango con una sola expresión.

**Lo típico que sale mal**
- Separar el rango en dos condiciones y olvidarse de una.
- Usar límites incorrectos.

## Más allá (nivel pro)
Las condiciones complejas se vuelven más legibles si nombras cada parte.

**Aprende esto**
- Aprenderás a escribir condiciones complejas sin perder claridad.
- Verás cómo reutilizar una condición en varios lugares.

**Haz esto**
```
edad = 19  # Edad del usuario
puntos = 85  # Puntos acumulados
es_adulto = edad >= 18  # Condición reutilizable
tiene_puntos = puntos >= 80  # Otra condición
aprobado = es_adulto and tiene_puntos  # Condición compuesta
print(aprobado)  # Mostramos el resultado
```

**Verás esto**
Verás `True`.

**Por qué funciona**
Separar condiciones en variables hace el código más legible y fácil de probar.

**Lo típico que sale mal**
- Escribir condiciones largas en una sola línea sin claridad.
- Repetir la misma condición en varios lugares.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            ("Usar = en comparaciones", "El operador de comparación es ==, no =."),
            ("Olvidar else", "Si necesitas un camino alterno, agrega else."),
            ("Orden incorrecto en elif", "Coloca primero las condiciones más específicas."),
            ("Comparar texto sin normalizar", "Usa strip() y lower() para comparar strings."),
            ("Confundir and/or", "and exige ambas condiciones; or permite cualquiera."),
            ("Condiciones demasiado largas", "Divide la lógica en variables con nombres claros."),
            ("Usar if repetidos", "Encadena con elif para evitar múltiples ejecuciones."),
            ("Olvidar paréntesis en lógica compleja", "Asegura el orden correcto de evaluación."),
            ("Comparar None con ==", "Usa is None para comprobar ausencia de valor."),
            ("Usar valores mágicos", "Guarda límites en variables con nombres claros."),
            ("Ignorar el rango inclusivo", "En 20 <= x <= 25, los límites se incluyen."),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "if/else básico",
                """# Aprende esto
# Aprenderás a tomar una decisión simple.
# Verás cómo usar else para el caso contrario.
#
# Haz esto
edad = 20  # Edad del usuario
es_mayor = edad >= 18  # Condición booleana
if es_mayor:  # Si es verdadero
    mensaje = "Puede ingresar"  # Mensaje positivo
else:  # Caso contrario
    mensaje = "No puede ingresar"  # Mensaje negativo
print(mensaje)  # Mostramos el resultado
#
# Verás esto
# Verás "Puede ingresar".
#
# Por qué funciona
# La condición es True y el bloque if se ejecuta.
#
# Lo típico que sale mal
# - Usar = en lugar de ==.
# - Olvidar el else cuando aplica.
""",
            ),
            (
                "elif con rangos",
                """# Aprende esto
# Aprenderás a evaluar varias condiciones.
# Verás cómo elegir un solo resultado.
#
# Haz esto
puntaje = 75  # Puntaje del examen
if puntaje >= 90:  # Primer nivel
    nivel = "Excelente"  # Nivel alto
elif puntaje >= 70:  # Segundo nivel
    nivel = "Aprobado"  # Nivel medio
else:  # Caso restante
    nivel = "Reprobado"  # Nivel bajo
print(nivel)  # Mostramos el nivel
#
# Verás esto
# Verás "Aprobado".
#
# Por qué funciona
# Se ejecuta la primera condición verdadera.
#
# Lo típico que sale mal
# - Ordenar mal las condiciones.
# - Usar if separados en lugar de elif.
""",
            ),
            (
                "Condiciones con and",
                """# Aprende esto
# Aprenderás a combinar dos requisitos.
# Verás cómo usar and para exigir ambos.
#
# Haz esto
edad = 22  # Edad del usuario
saldo = 50  # Saldo disponible
es_adulto = edad >= 18  # Condición 1
saldo_ok = saldo >= 30  # Condición 2
if es_adulto and saldo_ok:  # Ambas condiciones
    estado = "Compra permitida"  # Resultado positivo
else:  # Si falla alguna
    estado = "Compra rechazada"  # Resultado negativo
print(estado)  # Mostramos el resultado
#
# Verás esto
# Verás "Compra permitida".
#
# Por qué funciona
# and exige que ambas condiciones sean True.
#
# Lo típico que sale mal
# - Usar or en lugar de and.
# - No separar condiciones en variables.
""",
            ),
            (
                "Comparación de texto",
                """# Aprende esto
# Aprenderás a comparar texto con normalización.
# Verás cómo evitar errores por espacios.
#
# Haz esto
entrada = "  Si "  # Texto del usuario
respuesta = entrada.strip().lower()  # Normalizamos
if respuesta == "si":  # Comparamos con el esperado
    mensaje = "Confirmado"  # Resultado positivo
else:  # Caso contrario
    mensaje = "Cancelado"  # Resultado negativo
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Confirmado".
#
# Por qué funciona
# strip y lower limpian el texto antes de comparar.
#
# Lo típico que sale mal
# - Comparar sin limpiar.
# - Olvidar lower.
""",
            ),
            (
                "Rango con comparación encadenada",
                """# Aprende esto
# Aprenderás a validar rangos con una sola expresión.
# Verás cómo crear un estado legible.
#
# Haz esto
temperatura = 23  # Temperatura actual
if 20 <= temperatura <= 25:  # Validamos rango
    estado = "Confort"  # Estado adecuado
else:  # Fuera del rango
    estado = "Ajustar"  # Mensaje alternativo
print(estado)  # Mostramos el estado
#
# Verás esto
# Verás "Confort".
#
# Por qué funciona
# La comparación encadenada verifica ambos límites.
#
# Lo típico que sale mal
# - Separar en dos condiciones y olvidar una.
# - Usar límites incorrectos.
""",
            ),
            (
                "Operador or",
                """# Aprende esto
# Aprenderás a permitir varias opciones válidas.
# Verás cómo usar or para aceptar cualquiera.
#
# Haz esto
metodo = "tarjeta"  # Método de pago
if metodo == "tarjeta" or metodo == "transferencia":  # Opciones válidas
    mensaje = "Pago aceptado"  # Resultado positivo
else:  # Opción no válida
    mensaje = "Pago rechazado"  # Resultado negativo
print(mensaje)  # Mostramos el mensaje
#
# Verás esto
# Verás "Pago aceptado".
#
# Por qué funciona
# or permite que cualquiera de las condiciones sea True.
#
# Lo típico que sale mal
# - Usar and cuando solo se necesita una opción.
# - No cubrir el else.
""",
            ),
            (
                "Negación con not",
                """# Aprende esto
# Aprenderás a negar una condición.
# Verás cómo interpretar not en el flujo.
#
# Haz esto
activo = False  # Estado inicial
if not activo:  # Negamos la condición
    mensaje = "Cuenta inactiva"  # Mensaje de alerta
else:  # Si está activa
    mensaje = "Cuenta activa"  # Mensaje positivo
print(mensaje)  # Mostramos el resultado
#
# Verás esto
# Verás "Cuenta inactiva".
#
# Por qué funciona
# not invierte el valor booleano.
#
# Lo típico que sale mal
# - Usar not con condiciones confusas.
# - Doble negación innecesaria.
""",
            ),
            (
                "Condición compuesta legible",
                """# Aprende esto
# Aprenderás a dividir condiciones complejas.
# Verás cómo reutilizar variables booleanas.
#
# Haz esto
edad = 19  # Edad del usuario
puntos = 85  # Puntos acumulados
es_adulto = edad >= 18  # Condición 1
puntaje_ok = puntos >= 80  # Condición 2
aprobado = es_adulto and puntaje_ok  # Condición compuesta
print(aprobado)  # Mostramos el resultado
#
# Verás esto
# Verás True.
#
# Por qué funciona
# Las variables booleanas hacen la condición más clara.
#
# Lo típico que sale mal
# - Escribir todo en una sola línea.
# - Repetir condiciones en varios lugares.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Crea una condición que imprima 'Adulto' si edad >= 18.",
                "hints": ["Usa if"],
                "solution": "edad = 20\nif edad >= 18:\n    print('Adulto')",
            },
            {
                "question": "Usa elif para clasificar un puntaje en alto, medio o bajo.",
                "hints": [">= 90, >= 70, else"],
                "solution": "puntaje = 75\nif puntaje >= 90:\n    print('Alto')\nelif puntaje >= 70:\n    print('Medio')\nelse:\n    print('Bajo')",
            },
            {
                "question": "Valida que un usuario sea mayor de edad y tenga saldo suficiente.",
                "hints": ["Usa and"],
                "solution": "edad = 20\nsaldo = 50\nif edad >= 18 and saldo >= 30:\n    print('Ok')",
            },
            {
                "question": "Normaliza una respuesta y compara si es 'si'.",
                "hints": ["Usa strip y lower"],
                "solution": "respuesta = ' Si '\ntexto = respuesta.strip().lower()\nif texto == 'si':\n    print('Confirmado')",
            },
            {
                "question": "Verifica si un valor está entre 10 y 20.",
                "hints": ["Usa comparación encadenada"],
                "solution": "valor = 15\nif 10 <= valor <= 20:\n    print('En rango')",
            },
            {
                "question": "Acepta método de pago 'tarjeta' o 'transferencia'.",
                "hints": ["Usa or"],
                "solution": "metodo = 'tarjeta'\nif metodo == 'tarjeta' or metodo == 'transferencia':\n    print('Aceptado')",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget

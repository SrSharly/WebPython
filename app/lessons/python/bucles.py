from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.lesson_base import Lesson


class BuclesLesson(Lesson):
    TITLE = "Bucles"
    CATEGORY = "Python"
    SUBCATEGORY = "Fundamentos"
    LEVEL = "Básico"
    TAGS = ["for", "while", "iteración", "range"]

    def summary(self) -> str:
        return (
            "Aprende desde cero a repetir tareas con for y while, entender range, "
            "y controlar bucles con break y continue de forma segura."
        )

    def guide(self) -> str:
        return self.tutorial()

    def tutorial(self) -> str:
        return """
## Introducción: repetir con intención
Los bucles sirven para repetir una tarea sin copiar el mismo código. Son esenciales para recorrer listas, sumar valores,
procesar archivos o repetir intentos hasta cumplir una condición. En esta lección aprenderás a usar `for` y `while`,
controlar el flujo con `break` y `continue`, y escribir bucles que sean claros y seguros.

## Paso 1: for con listas
El bucle `for` recorre elementos de una secuencia en orden.

**Aprende esto**
- Aprenderás a iterar sobre una lista de forma simple.
- Verás cómo acumular resultados en cada iteración.

**Haz esto**
print("ok")  # Confirmamos
print("---")  # Separador
```
frutas = ["manzana", "pera", "uva"]  # Lista de frutas
conteo = 0  # Contador inicial
for fruta in frutas:  # Recorremos cada fruta
    conteo = conteo + 1  # Incrementamos el contador
    mensaje = "Fruta: " + fruta  # Construimos un mensaje
    print(mensaje)  # Mostramos la fruta
print(conteo)  # Mostramos el total
print("ok")  # Confirmamos
print("---")  # Separador
```

**Verás esto**
Verás cada fruta en una línea y el número 3 al final.

**Por qué funciona**
`for` toma cada elemento de la lista y lo asigna a la variable de iteración. El contador suma uno por elemento.

**Lo típico que sale mal**
- Modificar la lista mientras la recorres.
- Reutilizar una variable del bucle fuera de contexto.

## Paso 2: for con range
`range()` genera secuencias de números útiles para repetir un número fijo de veces.

**Aprende esto**
- Aprenderás a usar `range()` para iterar con índices.
- Verás cómo sumar valores dentro de un rango.

**Haz esto**
print("ok")  # Confirmamos
print("---")  # Separador
```
limite = 5  # Definimos el límite
suma = 0  # Acumulador
for i in range(limite):  # Iteramos de 0 a 4
    suma = suma + i  # Acumulamos el valor
    print(i)  # Mostramos el índice
print(suma)  # Mostramos la suma total
print(range(limite))  # Mostramos el objeto range
print("ok")  # Confirmamos
print("---")  # Separador
```

**Verás esto**
Verás los números 0 a 4, la suma 10 y una representación de `range(0, 5)`.

**Por qué funciona**
`range(limite)` produce una secuencia de enteros desde 0 hasta `limite - 1`, y puedes sumar cada valor.

**Lo típico que sale mal**
- Esperar que `range(5)` incluya el 5.
- Confundir `range` con una lista y tratar de imprimirla igual.

## Paso 3: while con condición
`while` repite mientras una condición sea verdadera. Es útil cuando no sabes cuántas iteraciones habrá.

**Aprende esto**
- Aprenderás a controlar un bucle con una condición.
- Verás cómo evitar bucles infinitos.

**Haz esto**
print("ok")  # Confirmamos
print("---")  # Separador
```
intentos = 0  # Contador inicial
max_intentos = 3  # Límite de intentos
while intentos < max_intentos:  # Condición del bucle
    intentos = intentos + 1  # Incrementamos intentos
    mensaje = "Intento " + str(intentos)  # Mensaje
    print(mensaje)  # Mostramos el intento
print("Fin")  # Indicamos fin
print("ok")  # Confirmamos
print("---")  # Separador
```

**Verás esto**
Verás `Intento 1`, `Intento 2`, `Intento 3` y `Fin`.

**Por qué funciona**
El bucle continúa mientras `intentos < max_intentos` sea verdadero. Cuando se iguala, el bucle termina.

**Lo típico que sale mal**
- Olvidar incrementar el contador y causar un bucle infinito.
- Usar una condición mal planteada que nunca se cumple.

## Paso 4: break y continue
Estas palabras controlan el flujo dentro del bucle: `break` sale y `continue` salta a la siguiente iteración.

**Aprende esto**
- Aprenderás cuándo cortar un bucle con `break`.
- Verás cómo omitir un caso con `continue`.

**Haz esto**
print("ok")  # Confirmamos
print("---")  # Separador
```
numeros = [1, 2, 3, 4, 5]  # Lista de números
for n in numeros:  # Recorremos la lista
    if n == 3:  # Si es 3
        continue  # Saltamos esta iteración
    if n == 5:  # Si es 5
        break  # Terminamos el bucle
    print(n)  # Mostramos el número
print("Listo")  # Indicamos fin
print("ok")  # Confirmamos
print("---")  # Separador
```

**Verás esto**
Verás `1`, `2`, `4` y luego `Listo`.

**Por qué funciona**
`continue` salta el resto del bloque y `break` termina el bucle por completo cuando la condición se cumple.

**Lo típico que sale mal**
- Abusar de `break` y ocultar lógica necesaria.
- Usar `continue` sin actualizar variables y generar bucles infinitos.

## Paso 5: enumerate para índices
`enumerate()` permite recorrer elementos y obtener su índice sin usar `range`.

**Aprende esto**
- Aprenderás a usar `enumerate()` para índices legibles.
- Verás cómo construir mensajes con índice y valor.

**Haz esto**
print("ok")  # Confirmamos
print("---")  # Separador
```
frutas = ["manzana", "pera", "uva"]  # Lista de frutas
for indice, fruta in enumerate(frutas, start=1):  # Recorremos con índice
    etiqueta = "#" + str(indice)  # Construimos etiqueta
    mensaje = etiqueta + " " + fruta  # Mensaje final
    print(mensaje)  # Mostramos mensaje
print("Total: " + str(len(frutas)))  # Mostramos total
print("ok")  # Confirmamos
print("---")  # Separador
```

**Verás esto**
Verás etiquetas como `#1 manzana` y el total 3.

**Por qué funciona**
`enumerate` entrega pares `(índice, valor)` y `start=1` ajusta el índice para humanos.

**Lo típico que sale mal**
- Usar índices manuales y desincronizarlos.
- Olvidar que `start` es opcional.

## Paso 6: Bucles anidados con cuidado
Los bucles dentro de bucles son potentes, pero debes controlar el tamaño para no hacer trabajo innecesario.

**Aprende esto**
- Aprenderás a anidar bucles para comparar elementos.
- Verás cómo mantener el control del conteo.

**Haz esto**
print("ok")  # Confirmamos
print("---")  # Separador
```
filas = ["A", "B"]  # Identificadores de filas
columnas = [1, 2, 3]  # Identificadores de columnas
conteo = 0  # Contador
for fila in filas:  # Primer bucle
    for col in columnas:  # Segundo bucle
        celda = fila + str(col)  # Construimos el identificador
        print(celda)  # Mostramos la celda
        conteo = conteo + 1  # Contamos celdas
print(conteo)  # Mostramos el total
print("ok")  # Confirmamos
print("---")  # Separador
```

**Verás esto**
Verás `A1`, `A2`, `A3`, `B1`, `B2`, `B3` y el total 6.

**Por qué funciona**
El bucle externo recorre filas y el interno recorre columnas, creando todas las combinaciones posibles.

**Lo típico que sale mal**
- Crear bucles anidados sin medir el tamaño y generar demasiado trabajo.
- Usar variables del bucle interno fuera de contexto.

## Más allá (nivel pro): acumuladores y patrones seguros
En proyectos reales, los bucles se usan para sumar, filtrar o construir resultados nuevos de forma explícita.

**Aprende esto**
- Aprenderás a usar acumuladores para resultados confiables.
- Verás un patrón seguro para construir listas nuevas.

**Haz esto**
print("ok")  # Confirmamos
print("---")  # Separador
```
ventas = [100, 200, 150]  # Lista de ventas
acumulado = 0  # Acumulador inicial
for monto in ventas:  # Recorremos ventas
    acumulado = acumulado + monto  # Sumamos
promedio = acumulado / len(ventas)  # Calculamos promedio
ventas_altas = []  # Lista de ventas altas
for monto in ventas:  # Recorremos otra vez
    if monto >= 150:  # Filtramos
        ventas_altas.append(monto)  # Guardamos
print(promedio)  # Mostramos promedio
print(ventas_altas)  # Mostramos filtradas
print("ok")  # Confirmamos
print("---")  # Separador
```

**Verás esto**
Verás el promedio y la lista `[200, 150]`.

**Por qué funciona**
El acumulador suma cada monto y luego se divide por la cantidad. La lista nueva guarda solo valores que cumplen la regla.

**Lo típico que sale mal**
- Reusar la lista original y modificarla dentro del bucle.
- Dividir por cero si la lista está vacía.
""".strip()

    def common_pitfalls(self) -> list[tuple[str, str]]:
        return [
            (
                "Bucle infinito",
                "Olvidar actualizar la condición en while provoca bucles infinitos.",
            ),
            (
                "Modificar la lista mientras iteras",
                "Puede saltar elementos o provocar resultados inesperados.",
            ),
            (
                "Confundir rango",
                "range(5) llega hasta 4, no hasta 5.",
            ),
            (
                "No inicializar acumuladores",
                "Si no defines el acumulador, la suma falla.",
            ),
            (
                "Abusar de break",
                "Salir del bucle sin razón clara puede ocultar errores.",
            ),
            (
                "Usar continue mal",
                "Saltarse pasos puede dejar variables sin actualizar.",
            ),
            (
                "Olvidar enumerate",
                "Usar range(len(lista)) complica el código sin necesidad.",
            ),
            (
                "Bucles anidados excesivos",
                "Crean complejidad y problemas de rendimiento.",
            ),
            (
                "No manejar lista vacía",
                "Dividir por len(lista) falla si está vacía.",
            ),
            (
                "Reusar nombres",
                "Usar el mismo nombre para variables internas confunde el flujo.",
            ),
            (
                "No cerrar recursos",
                "En archivos, olvidarlo deja recursos abiertos.",
            ),
            (
                "Confundir for con while",
                "Usar while cuando un for sería más claro.",
            ),
        ]

    def code_examples(self) -> list[tuple[str, str]]:
        return [
            (
                "for sobre lista",
                """# Aprende esto
# Aprenderás a recorrer una lista con for.
# Verás cómo contar elementos.
# Practicarás la construcción de mensajes.
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista de frutas
conteo = 0  # Contador inicial
for fruta in frutas:  # Recorremos cada fruta
    conteo = conteo + 1  # Incrementamos contador
    mensaje = "Fruta: " + fruta  # Mensaje
    print(mensaje)  # Mostramos fruta
    print(len(fruta))  # Mostramos longitud de la fruta
print(conteo)  # Mostramos total
#
# Verás esto
# Verás cada fruta y el total 3.
#
# Por qué funciona
# for toma cada elemento y lo asigna a la variable de iteración.
#
# Lo típico que sale mal
# - Modificar la lista mientras iteras.
# - Reutilizar la variable fuera del bucle.
""",
            ),
            (
                "for con range",
                """# Aprende esto
# Aprenderás a usar range para índices.
# Verás cómo sumar valores del rango.
# Entenderás el límite superior.
#
# Haz esto
limite = 5  # Límite del rango
suma = 0  # Acumulador
for i in range(limite):  # Iteramos de 0 a 4
    suma = suma + i  # Sumamos el índice
    print(i)  # Mostramos el índice
print(suma)  # Mostramos la suma
print(range(limite))  # Mostramos el range
print(type(suma))  # Mostramos el tipo de suma
#
# Verás esto
# Verás 0 a 4 y la suma 10.
#
# Por qué funciona
# range produce números hasta limite - 1.
#
# Lo típico que sale mal
# - Esperar que range incluya el límite.
# - Usar range como lista sin convertir.
""",
            ),
            (
                "while controlado",
                """# Aprende esto
# Aprenderás a usar while con contador.
# Verás cómo detener el bucle correctamente.
# Evitarás bucles infinitos.
#
# Haz esto
intentos = 0  # Contador
max_intentos = 3  # Límite
while intentos < max_intentos:  # Condición
    intentos = intentos + 1  # Incrementamos
    mensaje = "Intento " + str(intentos)  # Mensaje
    print(mensaje)  # Mostramos
print("Fin")  # Indicamos fin
print(intentos)  # Mostramos el contador final
#
# Verás esto
# Verás intentos 1 a 3 y "Fin".
#
# Por qué funciona
# El contador cambia hasta que la condición deja de cumplirse.
#
# Lo típico que sale mal
# - Olvidar incrementar el contador.
# - Usar una condición que nunca cambia.
""",
            ),
            (
                "break y continue",
                """# Aprende esto
# Aprenderás a usar break y continue.
# Verás cómo controlar el flujo dentro del bucle.
# Evitarás iteraciones innecesarias.
#
# Haz esto
numeros = [1, 2, 3, 4, 5]  # Lista de números
for n in numeros:  # Recorremos
    if n == 3:  # Si es 3
        continue  # Saltamos
    if n == 5:  # Si es 5
        break  # Terminamos
    print(n)  # Mostramos el número
print("Listo")  # Indicamos fin
#
# Verás esto
# Verás 1, 2, 4 y luego "Listo".
#
# Por qué funciona
# continue salta la iteración y break termina el bucle.
#
# Lo típico que sale mal
# - Usar break sin justificar.
# - Usar continue sin actualizar variables.
""",
            ),
            (
                "enumerate con índice",
                """# Aprende esto
# Aprenderás a usar enumerate para índices.
# Verás cómo construir etiquetas legibles.
# Evitarás usar range(len()).
#
# Haz esto
frutas = ["manzana", "pera", "uva"]  # Lista
for indice, fruta in enumerate(frutas, start=1):  # Índice desde 1
    etiqueta = "#" + str(indice)  # Etiqueta
    mensaje = etiqueta + " " + fruta  # Mensaje
    print(mensaje)  # Mostramos
print("Total: " + str(len(frutas)))  # Total
print(frutas[0])  # Mostramos el primer elemento
print(frutas[-1])  # Mostramos el último elemento
#
# Verás esto
# Verás etiquetas #1, #2, #3 y el total.
#
# Por qué funciona
# enumerate entrega índice y valor en cada iteración.
#
# Lo típico que sale mal
# - Olvidar start y obtener índice desde 0.
# - Mezclar índices manuales.
""",
            ),
            (
                "Bucles anidados",
                """# Aprende esto
# Aprenderás a anidar bucles para combinaciones.
# Verás cómo contar combinaciones.
# Controlarás el tamaño del proceso.
#
# Haz esto
filas = ["A", "B"]  # Filas
columnas = [1, 2, 3]  # Columnas
conteo = 0  # Contador
for fila in filas:  # Bucle externo
    for col in columnas:  # Bucle interno
        celda = fila + str(col)  # Celda
        print(celda)  # Mostramos celda
        conteo = conteo + 1  # Contamos
print(conteo)  # Total
#
# Verás esto
# Verás A1 a B3 y el total 6.
#
# Por qué funciona
# Se generan todas las combinaciones posibles.
#
# Lo típico que sale mal
# - No controlar el tamaño del bucle.
# - Usar variables internas fuera del alcance.
""",
            ),
            (
                "Acumulador simple",
                """# Aprende esto
# Aprenderás a sumar valores con un acumulador.
# Verás cómo calcular un promedio.
# Mantendrás el flujo explícito.
#
# Haz esto
ventas = [100, 200, 150]  # Lista de ventas
acumulado = 0  # Acumulador
for monto in ventas:  # Recorremos ventas
    acumulado = acumulado + monto  # Sumamos
promedio = acumulado / len(ventas)  # Calculamos promedio
print(acumulado)  # Mostramos suma
print(promedio)  # Mostramos promedio
print(len(ventas))  # Mostramos cantidad
#
# Verás esto
# Verás 450, 150.0 y 3.
#
# Por qué funciona
# Se suma cada monto y se divide por la cantidad total.
#
# Lo típico que sale mal
# - Dividir por cero si la lista está vacía.
# - No inicializar el acumulador.
""",
            ),
            (
                "Filtrar en bucle",
                """# Aprende esto
# Aprenderás a filtrar valores con condiciones.
# Verás cómo construir una lista nueva.
# Evitarás modificar la lista original.
#
# Haz esto
ventas = [100, 200, 150]  # Lista de ventas
ventas_altas = []  # Lista vacía
for monto in ventas:  # Recorremos ventas
    if monto >= 150:  # Condición de filtro
        ventas_altas.append(monto)  # Agregamos
print(ventas_altas)  # Mostramos filtradas
print(len(ventas_altas))  # Cantidad filtrada
print(len(ventas))  # Cantidad total
#
# Verás esto
# Verás [200, 150], la cantidad 2 y el total 3.
#
# Por qué funciona
# append agrega solo los valores que cumplen la condición.
#
# Lo típico que sale mal
# - Modificar la lista original al iterar.
# - Olvidar inicializar la lista nueva.
""",
            ),
        ]

    def exercises(self) -> list[dict]:
        return [
            {
                "question": "Recorre una lista de nombres y muestra cada uno.",
                "hints": ["Usa for"],
                "solution": "nombres = ['Ana', 'Luis']\nfor nombre in nombres:\n    print(nombre)",
            },
            {
                "question": "Suma los números del 0 al 4 con range.",
                "hints": ["Usa range(5)"],
                "solution": "suma = 0\nfor i in range(5):\n    suma += i\nprint(suma)",
            },
            {
                "question": "Usa while para contar de 1 a 3.",
                "hints": ["Incrementa el contador"],
                "solution": "contador = 0\nwhile contador < 3:\n    contador += 1\n    print(contador)",
            },
            {
                "question": "Usa break para salir cuando el número sea 3.",
                "hints": ["Usa if n == 3"],
                "solution": "for n in [1, 2, 3, 4]:\n    if n == 3:\n        break\n    print(n)",
            },
            {
                "question": "Muestra índices y valores con enumerate.",
                "hints": ["Usa enumerate(lista)"],
                "solution": "lista = ['a', 'b']\nfor i, v in enumerate(lista):\n    print(i, v)",
            },
            {
                "question": "Filtra números mayores a 10 en una lista.",
                "hints": ["Crea una lista nueva"],
                "solution": "numeros = [5, 12, 3, 20]\nfiltrados = []\nfor n in numeros:\n    if n > 10:\n        filtrados.append(n)\nprint(filtrados)",
            },
        ]

    def build_demo(self) -> QWidget | None:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Esta lección es conceptual y no requiere demo interactiva."))
        return widget
